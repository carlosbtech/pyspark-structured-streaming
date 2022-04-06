import pyspark.sql.functions as f

from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .appName('Spark Structured Streaming')
    .getOrCreate()
)

spark.sparkContext.setLogLevel('ERROR')

# input data
lines = (
    spark
    .readStream
    .format('socket')
    .option('host', 'localhost')
    .option('port', 9999)
    .load()
)

print(type(lines))

# query
words = lines.select(
    f.explode(
        f.split(lines.value, ' ')
    ).alias('word')
)

wordCounts = words.groupBy('word').count()

# output
query = (
    wordCounts
    .writeStream
    .outputMode('complete')
    .format('console')
    .start()
)

query.awaitTermination()