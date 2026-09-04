# Data transformation
# Retail Data Engineering Pipeline

from pyspark.sql import functions as F
from pyspark.sql.window import Window


def trim_string_columns(df):
    """Trim whitespace from all string columns."""
    for column_name, data_type in df.dtypes:
        if data_type == "string":
            df = df.withColumn(
                column_name,
                F.trim(F.col(column_name))
            )
    return df


def convert_date_columns(df, columns):
    """Convert specified columns to date format."""
    for column_name in columns:
        df = df.withColumn(
            column_name,
            F.to_date(F.col(column_name), "yyyy-MM-dd")
        )
    return df


def calculate_total_price(df):
    """Calculate the total line-item price."""
    return df.withColumn(
        "L_TOTALPRICE",
        F.col("L_EXTENDEDPRICE")
        * (1 - F.col("L_DISCOUNT"))
        * (1 + F.col("L_TAX"))
    )


# ---------------------------------------------------------
# Lineitem transformations
# ---------------------------------------------------------

lineitem_df = trim_string_columns(lineitem_df)

lineitem_df = convert_date_columns(
    lineitem_df,
    [
        "L_SHIPDATE",
        "L_COMMITDATE",
        "L_RECEIPTDATE"
    ]
)

lineitem_df = calculate_total_price(lineitem_df)


# ---------------------------------------------------------
# Filtering
# ---------------------------------------------------------

air_shipmode_df = lineitem_df.filter(
    F.col("L_SHIPMODE") == "AIR"
)


# ---------------------------------------------------------
# Aggregation
# ---------------------------------------------------------

avg_discount_df = (
    lineitem_df
    .groupBy("L_ORDERKEY")
    .agg(
        F.avg("L_DISCOUNT").alias("avg_discount")
    )
)


# ---------------------------------------------------------
# Window function
# ---------------------------------------------------------

window_spec = (
    Window
    .partitionBy("L_ORDERKEY")
    .orderBy(
        F.col("L_QUANTITY").desc()
    )
)

ranked_lineitem_df = lineitem_df.withColumn(
    "product_rank",
    F.rank().over(window_spec)
)


# ---------------------------------------------------------
# Display sample results
# ---------------------------------------------------------

air_shipmode_df.show(5)
avg_discount_df.show(5)
ranked_lineitem_df.show(5)
