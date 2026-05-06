import dlt
from pyspark.sql.functions import col, sum


@dlt.table(name="bronze_orders")
def bronze_orders():
    return spark.createDataFrame([
        (301,101,201,"2024-04-01",20,"Delivered"),
        (302,102,201,"2024-04-01",35,"Delivered"),
        (303,111,204,"2024-04-02",2,"Delivered"),
        (304,114,208,"2024-04-02",5,"Pending"),
        (305,115,204,"2024-04-03",3,"Delivered"),
        (306,104,202,"2024-04-03",50,"Delivered"),
        (307,105,202,"2024-04-04",18,"Cancelled")
    ],
    ["order_id","product_id","supplier_id","order_date","quantity","order_status"])


@dlt.table(name="silver_orders")
def silver_orders():
    df = dlt.read("bronze_orders")

    return df.filter(
        (col("order_status").isNotNull()) &
        (col("quantity") > 0)
    )


@dlt.table(name="silver_orders_enriched")
def silver_orders_enriched():
    df = dlt.read("silver_orders")

    return df.withColumn(
        "total_revenue",
        col("quantity") * 1000   
    )


@dlt.table(name="silver_clean_orders")
def silver_clean_orders():
    df = dlt.read("silver_orders_enriched")

    return df.filter(
        col("order_status").isin("Delivered", "Pending")
    )


@dlt.table(name="gold_city_revenue_v2")
def gold_city_revenue():
    df = dlt.read("silver_clean_orders")

    return df.groupBy("supplier_id").agg(
        sum("total_revenue").alias("city_revenue")
    )


@dlt.table(name="gold_category_revenue_v2")
def gold_category_revenue():
    df = dlt.read("silver_clean_orders")

    return df.groupBy("order_status").agg(
        sum("total_revenue").alias("category_revenue")
    )

