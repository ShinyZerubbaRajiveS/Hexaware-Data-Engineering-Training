#Tasks 
# 1. Create Bronze table (inline data) 
# 2. Create Silver table with transformations 
# 3. Create Gold table with aggregations 
# 4. Define proper dependencies 
# 5. Run the pipeline


import dlt
from pyspark.sql.functions import *

# 1. Bronze Table (Raw Data)

@dlt.table
def bronze_patient():
    data = [
        (101,"Arjun Reddy","Hyderabad","Cardiology",5000,1),
        (102,"Sneha Kapoor","Delhi","Orthopedics",3000,2),
        (103,"Rahul Sharma","Mumbai","Dermatology",1500,1),
        (104,"Priya Nair","Bangalore","Cardiology",5000,2),
        (105,"Vikram Singh","Chennai","Neurology",7000,1),
        (106,"Ananya Das","Kolkata","Orthopedics",3000,3),
        (107,"Karan Patel","Ahmedabad","Cardiology",5000,1),
        (108,"Meera Iyer","Bangalore","Dermatology",1500,2)
    ]

    columns = [
        "visit_id",
        "patient_name",
        "city",
        "department",
        "consultation_fee",
        "tests_count"
    ]

    return spark.createDataFrame(data, columns)


# 2. Silver Table (Transformation)

@dlt.table
def silver_patient():
    df = dlt.read("bronze_patient")

    return df.withColumn(
        "total_bill",
        col("consultation_fee") + col("tests_count") * 500
    ).withColumn(
        "patient_type",
        when(col("total_bill") >= 6000, "High")
        .when(col("total_bill") >= 4000, "Medium")
        .otherwise("Low")
    )


# 3. Gold Table (Aggregation)

@dlt.table
def gold_patient():
    df = dlt.read("silver_patient")

    return df.groupBy("department").agg(
        count("*").alias("total_patients"),
        sum("total_bill").alias("total_revenue"),
        avg("total_bill").alias("avg_bill")
    )