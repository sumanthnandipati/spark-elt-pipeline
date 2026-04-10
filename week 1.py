data = [
("Alice", 21, "Los Angeles"),
("Bob", 22, "San Bernardino"),
("Carol", 23, "Riverside"),
("David", 24, "Ontario"),
("Erin", 22, "Riverside"),
("Frank", 25, "Los Angeles"),
]
df = spark.createDataFrame(data, ["name", "age", "city"])
df.show()
df.createOrReplaceTempView("people")
spark.sql("SELECT * FROM people").show()
spark.sql("SELECT name, age, city FROM people WHERE age > 22").show()
spark.sql("""
SELECT city, COUNT(*) AS total_people
FROM people
GROUP BY city
""").show()
spark.sql("""
SELECT city, COUNT(*) AS total_people
FROM people
GROUP BY city
ORDER BY total_people DESC
""").show()
from pyspark.sql.functions import count
df.groupBy("city").agg(count("*").alias("total_people")).show()
