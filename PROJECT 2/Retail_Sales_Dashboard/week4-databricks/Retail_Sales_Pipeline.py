
# =========================================================
# IMPORTS
# =========================================================

import dlt

from pyspark.sql.functions import *


# =========================================================
# BRONZE SALES
# =========================================================

@dlt.table
def bronze_sales():

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/retail_catalog/retail_schema/raw_files/sales.csv")

    return df


# =========================================================
# BRONZE PRODUCTS
# =========================================================

@dlt.table
def bronze_products():

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/retail_catalog/retail_schema/raw_files/products.csv")

    return df


# =========================================================
# BRONZE STORES
# =========================================================

@dlt.table
def bronze_stores():

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/retail_catalog/retail_schema/raw_files/stores.csv")

    return df


# =========================================================
# BRONZE EMPLOYEES
# =========================================================

@dlt.table
def bronze_employees():

    df = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/retail_catalog/retail_schema/raw_files/employees.csv")

    return df


# =========================================================
# SILVER SALES
# =========================================================

@dlt.table
def silver_sales():

    df = dlt.read("bronze_sales")

    df = df.dropna()

    return df


# =========================================================
# SILVER PRODUCTS
# =========================================================

@dlt.table
def silver_products():

    df = dlt.read("bronze_products")

    df = df.dropna()

    df = df.withColumn(
        "category",
        upper(col("category"))
    )

    return df


# =========================================================
# SILVER STORES
# =========================================================

@dlt.table
def silver_stores():

    df = dlt.read("bronze_stores")

    df = df.dropna()

    df = df.withColumn(
        "region",
        upper(col("region"))
    )

    return df


# =========================================================
# SILVER EMPLOYEES
# =========================================================

@dlt.table
def silver_employees():

    df = dlt.read("bronze_employees")

    df = df.dropna()

    # REMOVE DUPLICATE COLUMN
    df = df.drop("store_id")

    return df


# =========================================================
# SILVER RETAIL ANALYTICS
# =========================================================

@dlt.table
def silver_retail_analytics():

    sales_df = dlt.read("silver_sales")

    products_df = dlt.read("silver_products")

    stores_df = dlt.read("silver_stores")

    employees_df = dlt.read("silver_employees")


    # =====================================================
    # JOIN SALES + PRODUCTS
    # =====================================================

    df = sales_df.join(
        products_df,
        sales_df["product_id"] == products_df["product_id"],
        "inner"
    ).drop(products_df["product_id"])


    # =====================================================
    # JOIN STORES
    # =====================================================

    df = df.join(
        stores_df,
        df["store_id"] == stores_df["store_id"],
        "inner"
    ).drop(stores_df["store_id"])


    # =====================================================
    # JOIN EMPLOYEES
    # =====================================================

    df = df.join(
        employees_df,
        df["employee_id"] == employees_df["employee_id"],
        "inner"
    ).drop(employees_df["employee_id"])


    # =====================================================
    # REVENUE
    # =====================================================

    df = df.withColumn(
        "revenue",
        col("quantity") * col("price")
    )


    # =====================================================
    # DISCOUNT AMOUNT
    # =====================================================

    df = df.withColumn(
        "discount_amount",
        col("revenue") *
        col("discount_percent") / 100
    )


    # =====================================================
    # FINAL REVENUE
    # =====================================================

    df = df.withColumn(
        "final_revenue",
        col("revenue") -
        col("discount_amount")
    )


    # =====================================================
    # PROFIT
    # =====================================================

    df = df.withColumn(
        "profit",
        col("final_revenue") -
        (col("quantity") * col("cost"))
    )

    return df


# =========================================================
# GOLD STORE KPIs
# =========================================================

@dlt.table
def gold_store_kpis():

    df = dlt.read("silver_retail_analytics")

    result = df.groupBy(
        "store_name"
    ).agg(

        round(
            sum("final_revenue"),
            2
        ).alias("total_revenue"),

        round(
            sum("profit"),
            2
        ).alias("total_profit"),

        round(
            avg("discount_percent"),
            2
        ).alias("avg_discount_percent"),

        count("sale_id")
            .alias("total_sales")
    )

    return result


# =========================================================
# GOLD TOP PRODUCTS
# =========================================================

@dlt.table
def gold_top_products():

    df = dlt.read("silver_retail_analytics")

    result = df.groupBy(
        "product_name"
    ).agg(

        sum("quantity")
            .alias("total_quantity_sold"),

        round(
            sum("final_revenue"),
            2
        ).alias("total_revenue")
    )

    result = result.orderBy(
        col("total_quantity_sold").desc()
    )

    return result


# =========================================================
# GOLD UNDERPERFORMING PRODUCTS
# =========================================================

@dlt.table
def gold_underperforming_products():

    df = dlt.read("silver_retail_analytics")

    result = df.filter(
        col("quantity") < 3
    )

    return result


# =========================================================
# GOLD REGION SALES REPORT
# =========================================================

@dlt.table
def gold_region_sales_report():

    df = dlt.read("silver_retail_analytics")

    result = df.groupBy(
        "region"
    ).agg(

        round(
            sum("final_revenue"),
            2
        ).alias("regional_revenue"),

        round(
            sum("profit"),
            2
        ).alias("regional_profit")
    )

    return result