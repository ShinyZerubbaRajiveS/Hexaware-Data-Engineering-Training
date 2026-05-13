# =========================================================
# IMPORTS
# =========================================================

import dlt

from pyspark.sql.functions import *


# =========================================================
# BRONZE EMPLOYEES
# =========================================================

@dlt.table
def bronze_employees():

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/employee_catalog/attendance_schema/raw_files/employees.csv")

    return df


# =========================================================
# BRONZE ATTENDANCE
# =========================================================

@dlt.table
def bronze_attendance():

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/employee_catalog/attendance_schema/raw_files/attendance.csv")

    return df


# =========================================================
# BRONZE TASKS
# =========================================================

@dlt.table
def bronze_tasks():

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/employee_catalog/attendance_schema/raw_files/tasks.csv")

    return df


# =========================================================
# SILVER EMPLOYEES
# =========================================================

@dlt.table
def silver_employees():

    df = dlt.read("bronze_employees")

    df = df.dropna()

    df = df.withColumn(
        "department",
        upper(col("department"))
    )

    return df


# =========================================================
# SILVER ATTENDANCE
# =========================================================

@dlt.table
def silver_attendance():

    df = dlt.read("bronze_attendance")

    df = df.dropna()

    # Calculate work hours
    df = df.withColumn(
        "work_hours",
        (
            unix_timestamp("clock_out", "HH:mm:ss") -
            unix_timestamp("clock_in", "HH:mm:ss")
        ) / 3600
    )

    # Remove absent employees
    df = df.filter(
        col("status") != "Absent"
    )

    return df


# =========================================================
# SILVER TASKS
# =========================================================

@dlt.table
def silver_tasks():

    df = dlt.read("bronze_tasks")

    df = df.dropna()

    return df


# =========================================================
# SILVER PRODUCTIVITY
# =========================================================

@dlt.table
def silver_employee_productivity():

    employees_df = dlt.read("silver_employees")

    attendance_df = dlt.read("silver_attendance")

    tasks_df = dlt.read("silver_tasks")

    # Join Employees + Attendance
    df = employees_df.join(
        attendance_df,
        "employee_id",
        "inner"
    )

    # Join Tasks
    df = df.join(
        tasks_df,
        "employee_id",
        "inner"
    )

    # Productivity score
    df = df.withColumn(
        "productivity_score",
        round(
            col("tasks_completed") / col("work_hours"),
            2
        )
    )

    return df


# =========================================================
# GOLD DEPARTMENT KPI
# =========================================================

@dlt.table
def gold_department_kpis():

    df = dlt.read("silver_employee_productivity")

    result = df.groupBy("department").agg(

        round(
            avg("work_hours"),
            2
        ).alias("avg_work_hours"),

        round(
            avg("productivity_score"),
            2
        ).alias("avg_productivity"),

        sum("tasks_completed")
            .alias("total_tasks_completed"),

        count("employee_id")
            .alias("employee_count")
    )

    return result


# =========================================================
# GOLD TOP PERFORMERS
# =========================================================

@dlt.table
def gold_top_performers():

    df = dlt.read("silver_employee_productivity")

    result = df.orderBy(
        col("productivity_score").desc()
    )

    return result


# =========================================================
# GOLD ABSENTEE REPORT
# =========================================================

@dlt.table
def gold_absentee_report():

    df = dlt.read("bronze_attendance")

    result = df.filter(
        col("status") == "Absent"
    )

    return result