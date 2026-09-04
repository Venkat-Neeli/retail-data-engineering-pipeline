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


def write_gold_parquet_tables(dataframes_to_write):
    """
    Write processed DataFrames to the Gold Parquet layer.
    """

    for table_name, df in dataframes_to_write.items():

        target_path = f"{GOLD_PATH}/{table_name}"

        (
            df.write
            .format("parquet")
            .mode("overwrite")
            .save(target_path)
        )

        print(
            f"Created Gold dataset: {table_name}"
        )
