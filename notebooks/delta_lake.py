# Delta Lake operations
# Retail Data Engineering Pipeline

from config import SILVER_PATH

from data_ingestion import dataframes
from data_transformation import lineitem_df
from data_enrichment import (
    geo_location_df,
    parts_info_df,
)


# ---------------------------------------------------------
# Prepare Silver datasets
# ---------------------------------------------------------

silver_dataframes = {
    "customers": dataframes["customer"],
    "lineitem": lineitem_df,
    "orders": dataframes["orders"],
    "supplier": dataframes["supplier"],
    "geo_location": geo_location_df,
    "parts_info": parts_info_df,
}


# ---------------------------------------------------------
# Write datasets as Delta tables
# ---------------------------------------------------------

for table_name, df in silver_dataframes.items():

    target_path = f"{SILVER_PATH}/{table_name}"

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(target_path)
    )

    print(f"Created Silver Delta table: {table_name}")
