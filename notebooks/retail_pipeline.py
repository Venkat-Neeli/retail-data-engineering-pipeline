# Databricks Pipeline Entry Point
# Retail Data Engineering Pipeline

from src.data_ingestion import dataframes
from src.data_cleaning import cleaned_dataframes
from src.data_transformation import lineitem_df
from src.data_enrichment import (
    geo_location_df,
    parts_info_df,
)

print("========================================")
print("Retail Data Engineering Pipeline")
print("========================================")


# ---------------------------------------------------------
# 1. Data Ingestion
# ---------------------------------------------------------

print("\n[1] Data ingestion completed")

for name, df in dataframes.items():
    print(f"  {name}: {df.count()} records")


# ---------------------------------------------------------
# 2. Data Cleaning
# ---------------------------------------------------------

print("\n[2] Data cleaning completed")

for name, df in cleaned_dataframes.items():
    print(f"  {name}: {df.count()} records")


# ---------------------------------------------------------
# 3. Data Transformation
# ---------------------------------------------------------

print("\n[3] Data transformation completed")

print(f"  Lineitem records: {lineitem_df.count()}")


# ---------------------------------------------------------
# 4. Data Enrichment
# ---------------------------------------------------------

print("\n[4] Data enrichment completed")

print(f"  GeoLocation records: {geo_location_df.count()}")
print(f"  PartsInfo records: {parts_info_df.count()}")


# ---------------------------------------------------------
# Pipeline status
# ---------------------------------------------------------

print("\n========================================")
print("Pipeline initialization completed")
print("========================================")


# ---------------------------------------------------------
# 5. Delta Lake - Silver Layer
# ---------------------------------------------------------

from src.delta_lake import silver_dataframes

print("\n[5] Silver Delta layer")

for name, df in silver_dataframes.items():
    print(f"  {name}: {df.count()} records")


# ---------------------------------------------------------
# 6. Gold Layer
# ---------------------------------------------------------

from src.gold_layer import (
    gold_dataframes,
    write_gold_parquet_tables,
)

print("\n[6] Gold layer")

for name, df in gold_dataframes.items():
    print(f"  {name}: {df.count()} records")

write_gold_parquet_tables(gold_dataframes)


# ---------------------------------------------------------
# Pipeline completion
# ---------------------------------------------------------

print("\n========================================")
print("Retail data pipeline completed")
print("========================================")
