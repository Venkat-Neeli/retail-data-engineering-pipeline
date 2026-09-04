# Data ingestion - Azure Retail Data Engineering Pipeline
# Data ingestion - Azure Retail Data Engineering Pipeline

import pandas as pd
import glob


def load_and_combine_csv(path):
    """Load all CSV files from a directory and combine them."""
    all_files = glob.glob(path + "/*.csv")

    dataframes = [
        pd.read_csv(file, sep="\t", header=0)
        for file in all_files
    ]

    return pd.concat(dataframes, axis=0, ignore_index=True)


# Source paths
base_path = "/dbfs/FileStore/Retail"

customer_df = load_and_combine_csv(f"{base_path}/customer")
lineitem_df = load_and_combine_csv(f"{base_path}/lineitem")
order_df = load_and_combine_csv(f"{base_path}/orders")
nation_df = load_and_combine_csv(f"{base_path}/nation")
part_df = load_and_combine_csv(f"{base_path}/part")
partsupp_df = load_and_combine_csv(f"{base_path}/partsupp")
region_df = load_and_combine_csv(f"{base_path}/region")
supplier_df = load_and_combine_csv(f"{base_path}/supplier")


# Store all datasets in a dictionary for easier management
dataframes = {
    "customer": customer_df,
    "lineitem": lineitem_df,
    "orders": order_df,
    "nation": nation_df,
    "part": part_df,
    "partsupp": partsupp_df,
    "region": region_df,
    "supplier": supplier_df,
}


# Basic record-count validation
for name, df in dataframes.items():
    print(f"{name}: {len(df)} records")
