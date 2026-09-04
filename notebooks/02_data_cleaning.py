# Data cleaning and validation
# Retail Data Engineering Pipeline

import pandas as pd


def clean_dataframe(df):
    """Clean a dataframe by replacing empty strings and removing duplicates."""
    df = df.replace("", None)
    df = df.drop_duplicates()
    return df


def validate_dataframe(name, df):
    """Display basic data-quality information."""
    print(f"\nDataset: {name}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print("\nNull values:")
    print(df.isnull().sum())


# Apply cleaning
cleaned_dataframes = {
    name: clean_dataframe(df)
    for name, df in dataframes.items()
}


# Validate each dataset
for name, df in cleaned_dataframes.items():
    validate_dataframe(name, df)
