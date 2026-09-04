# Gold layer
# Retail Data Engineering Pipeline

gold_base_path = "dbfs:/mnt/retail/gold"


# ---------------------------------------------------------
# Gold datasets
# ---------------------------------------------------------

gold_dataframes = {
    "customers": customer_df,
    "lineitem": lineitem_df,
    "orders": order_df,
    "supplier": supplier_df,
    "geo_location": geo_location_df,
    "parts_info": parts_info_df,
}


# ---------------------------------------------------------
# Write Gold data as Parquet
# ---------------------------------------------------------

for table_name, df in gold_dataframes.items():

    target_path = f"{gold_base_path}/{table_name}"

    (
        df.write
        .format("parquet")
        .mode("overwrite")
        .save(target_path)
    )

    print(f"Created Gold dataset: {table_name}")
