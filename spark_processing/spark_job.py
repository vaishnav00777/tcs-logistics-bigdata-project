from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LogisticsAnalytics") \
    .getOrCreate()

df = spark.read.csv(
    '../data/processed_logistics.csv',
    header=True,
    inferSchema=True
)

df.groupBy("route_id").count().show()
