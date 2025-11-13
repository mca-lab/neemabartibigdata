#!/usr/bin/env python3
"""
Module 2 – Data Cleaning
------------------------
Cleans GDP and Population datasets:
  - removes duplicates
  - handles missing values
  - converts datatypes
  - removes outliers (IQR)
  - saves cleaned data to data/processed/ as SINGLE CSV FILES
"""

import os
import shutil
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, percentile_approx, sum as spark_sum

# -----------------------
# 1️⃣ Spark Setup
# -----------------------
spark = SparkSession.builder \
    .appName("GDP_Population_Cleaning") \
    .getOrCreate()

# -----------------------
# 2️⃣ File Paths (Updated for Docker)
# -----------------------
RAW_DIR = "/app/data/raw"
CLEAN_DIR = "/app/data/processed"

os.makedirs(CLEAN_DIR, exist_ok=True)

GDP_FILE = f"{RAW_DIR}/gdp.csv"
POP_FILE = f"{RAW_DIR}/population.csv"

# -----------------------
# 3️⃣ Load Datasets
# -----------------------
gdp_df = spark.read.csv(GDP_FILE, header=True, inferSchema=True)
pop_df = spark.read.csv(POP_FILE, header=True, inferSchema=True)

print("\n📘 GDP Dataset Schema:")
gdp_df.printSchema()

print("\n📗 Population Dataset Schema:")
pop_df.printSchema()

# -----------------------
# 4️⃣ Remove Duplicates
# -----------------------
gdp_df = gdp_df.dropDuplicates()
pop_df = pop_df.dropDuplicates()

# -----------------------
# 5️⃣ Missing Values Summary
# -----------------------
def missing_values(df):
    return df.select([
        spark_sum(col(c).isNull().cast("int")).alias(c)
        for c in df.columns
    ])

print("\n🔍 Missing values in GDP:")
missing_values(gdp_df).show()

print("\n🔍 Missing values in Population:")
missing_values(pop_df).show()

# -----------------------
# 6️⃣ Handle Missing Data
# -----------------------
key_cols = ["Country Name", "Year", "Value"]
gdp_df = gdp_df.na.drop(subset=key_cols)
pop_df = pop_df.na.drop(subset=key_cols)

# -----------------------
# 7️⃣ Type Conversion
# -----------------------
gdp_df = gdp_df.withColumn("Value", col("Value").cast("double")).withColumn("Year", col("Year").cast("int"))
pop_df = pop_df.withColumn("Value", col("Value").cast("double")).withColumn("Year", col("Year").cast("int"))

# -----------------------
# 8️⃣ Remove Outliers using IQR
# -----------------------
def remove_outliers(df, column):
    """Remove outliers using IQR method with percentile_approx."""
    percentiles = df.select(
        percentile_approx(col(column), [0.25, 0.75]).alias("q")
    ).collect()[0]["q"]

    q1, q3 = percentiles
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    print(f"\nIQR bounds for {column}: [{lower}, {upper}]")

    return df.filter((col(column) >= lower) & (col(column) <= upper))

gdp_df = remove_outliers(gdp_df, "Value")
pop_df = remove_outliers(pop_df, "Value")

# -----------------------
# 9️⃣ Save as Single CSV File (FIXED)
# -----------------------
def save_single_csv(df, output_file_path):
    tmp_dir = output_file_path + "_tmp"

    # 1. Remove old file if exists
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    # 2. Remove old temp folder if exists
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    # 3. Write dataframe to a temp folder
    df.coalesce(1).write.csv(tmp_dir, header=True, mode="overwrite")

    # 4. Move part file to final output name
    for file in os.listdir(tmp_dir):
        if file.startswith("part-") and file.endswith(".csv"):
            shutil.move(os.path.join(tmp_dir, file), output_file_path)

    # 5. Delete temp folder
    shutil.rmtree(tmp_dir)

# -----------------------
# 🔟 Output file paths
# -----------------------
gdp_clean_file = "/app/data/processed/gdp_clean.csv"
pop_clean_file = "/app/data/processed/population_clean.csv"

# -----------------------
# 1️⃣1️⃣ Save final cleaned CSVs
# -----------------------
save_single_csv(gdp_df, gdp_clean_file)
save_single_csv(pop_df, pop_clean_file)

print("\n✅ Cleaned single-file CSV datasets saved to:")
print(f" - {gdp_clean_file}")
print(f" - {pop_clean_file}")

# -----------------------
# 🔚 Stop Spark
# -----------------------
spark.stop()
