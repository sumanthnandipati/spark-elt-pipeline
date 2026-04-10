raw_data = [
("101", "Alice", "CA", 120.5),
("102", "Bob", "NV", 85.0),
("103", "Carol", "CA", 230.0),
("104", "David", "AZ", 50.0),
("105", "Eve", "NV", 300.0),
]
columns = ["order_id", "customer", "state", "amount"]
df_raw = spark.createDataFrame(raw_data, columns)
df_raw.show()

df_raw.printSchema()

from pyspark.sql.functions import col
df_clean = df_raw.withColumn("amount", col("amount").cast("double"))
df_state_sales = df_clean.groupBy("state").sum("amount")
df_state_sales.show()

df_clean.createOrReplaceTempView("state_sales")
spark.sql("""
SELECT state, SUM(amount) AS total_sales
FROM state_sales
GROUP BY state
ORDER BY total_sales DESC
""").show()
