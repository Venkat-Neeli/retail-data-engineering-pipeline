# Data enrichment and joins
# Retail Data Engineering Pipeline

from src.data_ingestion import dataframes


customer_df = dataframes["customer"]
order_df = dataframes["orders"]
nation_df = dataframes["nation"]
region_df = dataframes["region"]
part_df = dataframes["part"]
partsupp_df = dataframes["partsupp"]


# ---------------------------------------------------------
# Geography enrichment
# Nation + Region
# ---------------------------------------------------------

geo_location_df = (
    nation_df
    .join(
        region_df,
        nation_df["N_REGIONKEY"] == region_df["R_REGIONKEY"],
        "inner"
    )
    .select(
        nation_df["N_NATIONKEY"],
        nation_df["N_NAME"],
        region_df["R_REGIONKEY"],
        region_df["R_NAME"]
    )
)


# ---------------------------------------------------------
# Parts enrichment
# Part + Partsupp
# ---------------------------------------------------------

parts_info_df = (
    part_df
    .join(
        partsupp_df,
        part_df["P_PARTKEY"] == partsupp_df["PS_PARTKEY"],
        "inner"
    )
    .select(
        part_df["P_PARTKEY"],
        part_df["P_NAME"],
        part_df["P_MFGR"],
        part_df["P_BRAND"],
        part_df["P_TYPE"],
        part_df["P_SIZE"],
        part_df["P_CONTAINER"],
        part_df["P_RETAILPRICE"],
        partsupp_df["PS_SUPPKEY"],
        partsupp_df["PS_AVAILQTY"],
        partsupp_df["PS_SUPPLYCOST"]
    )
)


# ---------------------------------------------------------
# Customer + Orders enrichment
# ---------------------------------------------------------

customer_orders_df = (
    order_df
    .join(
        customer_df,
        order_df["O_CUSTKEY"] == customer_df["C_CUSTKEY"],
        "inner"
    )
    .select(
        order_df["O_ORDERKEY"],
        order_df["O_CUSTKEY"],
        order_df["O_ORDERSTATUS"],
        order_df["O_TOTALPRICE"],
        order_df["O_ORDERDATE"],
        customer_df["C_NAME"],
        customer_df["C_MKTSEGMENT"],
        customer_df["C_ACCTBAL"]
    )
)


# ---------------------------------------------------------
# Output
# ---------------------------------------------------------

print("Geography enrichment:")
geo_location_df.show(5)

print("Parts enrichment:")
parts_info_df.show(5)

print("Customer and order enrichment:")
customer_orders_df.show(5)
