# Data ingestion
# Retail Data Engineering Pipeline

import pandas as pd
import glob

from config import BASE_PATH


def load_and_combine_csv(path):
    """Load all CSV files from a directory and combine them."""

    all_files = glob.glob(f"{path}/*.csv")

    if not all_files:
        raise FileNotFoundError(
            f"No CSV files found in: {path}"
        )

    dataframes = [
        pd.read_csv(file, sep="\t", header=0)
        for file in all_files
    ]

    return pd.concat(
        dataframes,
        axis=0,
        ignore_index=True
    )


# ---------------------------------------------------------
# Load source datasets
# ---------------------------------------------------------

dataframes = {
    "customer": load_and_combine_csv(
        f"{BASE_PATH}/customer"
    ),

    "lineitem": load_and_combine_csv(
        f"{BASE_PATH}/lineitem"
    ),

    "orders": load_and_combine_csv(
        f"{BASE_PATH}/orders"
    ),

    "nation": load_and_combine_csv(
        f"{BASE_PATH}/nation"
    ),

    "part": load_and_combine_csv(
        f"{BASE_PATH}/part"
    ),

    "partsupp": load_and_combine_csv(
        f"{BASE_PATH}/partsupp"
    ),

    "region": load_and_combine_csv(
        f"{BASE_PATH}/region"
    ),

    "supplier": load_and_combine_csv(
        f"{BASE_PATH}/supplier"
    ),
}


# ---------------------------------------------------------
# Basic validation
# ---------------------------------------------------------

for name, df in dataframes.items():

    print(
        f"{name}: "
        f"{len(df)} records, "
        f"{len(df.columns)} columns"
    )
