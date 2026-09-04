# Databricks Pipeline Entry Point
# Retail Data Engineering Pipeline

from src.data_ingestion import dataframes
from src.data_cleaning import cleaned_dataframes
from src.data_transformation import lineitem_df
from src.data_enrichment import (
    geo_location_df,
    parts_info_df,
)

print("Retail data pipeline initialized successfully.")

print("\nDatasets:")
for name, df in dataframes.items():
    print(f"- {name}: {df.count()} records")

print("\nPipeline stages loaded:")
print("- Data ingestion")
print("- Data cleaning")
print("- Data transformation")
print("- Data enrichment")
print("- Delta Lake processing")
print("- Gold layer processing")
