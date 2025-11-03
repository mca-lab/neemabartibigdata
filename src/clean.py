from pyspark.sql import SparkSessio

spark = SparkSession.builder \
    .appName("GDP_Population_Cleaning") \
    .getOrCreate()
gdp_df = spark.read.csv("../data/raw/gdp.csv", header=True, inferSchema=True)
pop_df = spark.read.csv("../data/raw/population.csv", header=True, inferSchema=True)

print("GDP Dataset Schema:")
gdp_df.printSchema()

print("Population Dataset Schema:")
pop_df.printSchema()
gdp_df = gdp_df.dropDuplicates()
pop_df = pop_df.dropDuplicates()
from pyspark.sql.functions import col, sum as spark_sum

def missing_values(df):
    return df.select([spark_sum(col(c).isNull().cast("int")).alias(c) for c in df.columns])

print("Missing values in GDP:")
missing_values(gdp_df).show()

print("Missing values in Population:")
missing_values(pop_df).show()

# Example cleaning: drop rows missing the main columns
gdp_df = gdp_df.na.drop(subset=["Country", "Year", "GDP"])
pop_df = pop_df.na.drop(subset=["Country", "Year", "Population"])
from pyspark.sql.functions import col

gdp_df = gdp_df.withColumn("GDP", col("GDP").cast("double"))
pop_df = pop_df.withColumn("Population", col("Population").cast("double"))

gdp_df = gdp_df.withColumn("Year", col("Year").cast("int"))
pop_df = pop_df.withColumn("Year", col("Year").cast("int"))
def remove_outliers(df, column):
    stats = df.selectExpr(f'percentile({column}, array(0.25, 0.75)) as q').collect()[0]['q']
    q1, q3 = stats
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return df.filter((col(column) >= lower) & (col(column) <= upper))

gdp_df = remove_outliers(gdp_df, "GDP")
pop_df = remove_outliers(pop_df, "Population")
