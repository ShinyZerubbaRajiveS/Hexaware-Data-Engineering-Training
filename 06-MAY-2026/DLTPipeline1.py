import dlt
from pyspark.sql.functions import col

# 1. Create Bronze table using inline patient visit data

@dlt.table(
    name="bronze_patient_visits",
    comment="Raw patient visit data"
)
def bronze_patient_visits():
    data = [
        (1,"Chennai","Cardiology",2000,"Completed"),
        (2,"Bengaluru","Neurology",1500,"Completed"),
        (3,"Hyderabad","Orthopedic",None,"Pending"),
        (4,"Chennai","Cardiology",-500,"Completed"),  # invalid
        (5,"Mumbai","Dermatology",3000,"Completed")
    ]
    columns = ["visit_id","city","specialization","bill_amount","visit_status"]
    return spark.createDataFrame(data, columns)


# 2. Create Silver table with cleaned fields

@dlt.table(
    name="silver_patient_visits",
    comment="Cleaned patient visit data"
)
def silver_patient_visits():
    df = dlt.read("bronze_patient_visits")

    return df.filter(
        (col("bill_amount").isNotNull()) & 
        (col("bill_amount") > 0)
    )


@dlt.table(
    name="silver_patient_visits_enriched"
)
def silver_enriched():
    df = dlt.read("silver_patient_visits")

    return df.withColumn(
        "total_bill",
        col("bill_amount") + 500   
    )

# 5. Create Gold table grouped by city

@dlt.table(
    name="gold_city_revenue",
    comment="Revenue by city"
)
def gold_city():
    df = dlt.read("silver_patient_visits_enriched")

    return df.groupBy("city") \
        .sum("total_bill") \
        .withColumnRenamed("sum(total_bill)", "total_revenue")


# 6. Create Gold table grouped by specialization

@dlt.table(
    name="gold_specialization_revenue",
    comment="Revenue by specialization"
)
def gold_specialization():
    df = dlt.read("silver_patient_visits_enriched")

    return df.groupBy("specialization") \
        .sum("total_bill") \
        .withColumnRenamed("sum(total_bill)", "total_revenue")