# Data cleaning and validation
# Retail Data Engineering Pipeline

from pyspark.sql import functions as F

from src.data_ingestion import dataframes


def clean_dataframe(df):
    """Clean a dataframe by replacing empty strings and removing duplicates."""

    df = df.replace("", None)
    df = df.dropDuplicates()

    return df


def validate_dataframe(name, df):
    """Perform basic data-quality validation."""

    print(f"\nDataset: {name}")
    print(f"Rows: {df.count()}")
    print(f"Columns: {len(df.columns)}")

    null_counts = df.select([
        F.count(
            F.when(F.col(column).isNull(), column)
        ).alias(column)
        for column in df.columns
    ])

    print("Null values:")
    null_counts.show()


# ---------------------------------------------------------
# Clean datasets
# ---------------------------------------------------------

cleaned_dataframes = {
    name: clean_dataframe(df)
    for name, df in dataframes.items()
}


# ---------------------------------------------------------
# Validate datasets
# ---------------------------------------------------------

for name, df in cleaned_dataframes.items():
    validate_dataframe(name, df)
