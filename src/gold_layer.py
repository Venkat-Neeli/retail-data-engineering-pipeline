# Gold layer
# Retail Data Engineering Pipeline

from config import GOLD_PATH

from src.data_ingestion import dataframes
from src.data_transformation import lineitem_df
from src.data_enrichment import (
    geo_location_df,
    parts_info_df,
)


# ---------------------------------------------------------
# Prepare Gold datasets
# ---------------------------------------------------------

gold_dataframes = {
    "customers": dataframes["customer"],
    "lineitem": lineitem_df,
    "orders": dataframes["orders"],
    "supplier": dataframes["supplier"],
    "geo_location": geo_location_df,
    "parts_info": parts_info_df,
}


# ---------------------------------------------------------
# Write analytics-ready datasets
# ---------------------------------------------------------

for table_name, df in gold_dataframes.items():

    target_path = f"{GOLD_PATH}/{table_name}"

    (
        df.write
        .format("parquet")
        .mode("overwrite")
        .save(target_path)
    )

    print(f"Created Gold dataset: {table_name}")
