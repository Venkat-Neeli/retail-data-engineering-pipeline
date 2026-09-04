# Delta Lake operations
# Retail Data Engineering Pipeline

from config import SILVER_PATH
from src.data_ingestion import dataframes
from src.data_transformation import lineitem_df
from src.data_enrichment import (
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


def write_silver_delta_tables(dataframes_to_write):
    """
    Write processed DataFrames to the Silver Delta layer.
    """

    for table_name, df in dataframes_to_write.items():

        target_path = f"{SILVER_PATH}/{table_name}"

        (
            df.write
            .format("delta")
            .mode("overwrite")
            .option("overwriteSchema", "true")
            .save(target_path)
        )

        print(
            f"Created Silver Delta table: {table_name}"
        )
