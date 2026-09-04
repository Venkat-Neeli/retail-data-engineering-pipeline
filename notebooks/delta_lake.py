# Delta Lake operations
# Retail Data Engineering Pipeline

from delta.tables import DeltaTable


# ---------------------------------------------------------
# Silver layer paths
# ---------------------------------------------------------

silver_base_path = "dbfs:/mnt/retail/silver"


# ---------------------------------------------------------
# Write DataFrames as Delta tables
# ---------------------------------------------------------

silver_dataframes = {
    "customers": customer_df,
    "lineitem": lineitem_df,
    "orders": order_df,
    "supplier": supplier_df,
    "geo_location": geo_location_df,
    "parts_info": parts_info_df,
}


for table_name, df in silver_dataframes.items():

    target_path = f"{silver_base_path}/{table_name}"

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .save(target_path)
    )

    print(f"Created Delta table: {table_name}")
