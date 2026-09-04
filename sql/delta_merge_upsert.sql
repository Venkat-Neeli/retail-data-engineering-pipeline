-- =========================================================
-- Delta Lake MERGE / UPSERT
-- Retail Data Engineering Pipeline
--
-- Demonstrates how existing records are updated
-- and new records are inserted into a Delta table.
-- =========================================================

MERGE INTO lineitem AS target

USING lineitem_updates AS source

ON target.L_ORDERKEY = source.L_ORDERKEY
AND target.L_PARTKEY = source.L_PARTKEY
AND target.L_SUPPKEY = source.L_SUPPKEY

WHEN MATCHED THEN
    UPDATE SET
        target.L_QUANTITY = source.L_QUANTITY,
        target.L_EXTENDEDPRICE = source.L_EXTENDEDPRICE,
        target.L_DISCOUNT = source.L_DISCOUNT,
        target.L_TAX = source.L_TAX,
        target.L_RETURNFLAG = source.L_RETURNFLAG,
        target.L_LINESTATUS = source.L_LINESTATUS,
        target.L_SHIPDATE = source.L_SHIPDATE,
        target.L_COMMITDATE = source.L_COMMITDATE,
        target.L_RECEIPTDATE = source.L_RECEIPTDATE,
        target.L_SHIPINSTRUCT = source.L_SHIPINSTRUCT,
        target.L_SHIPMODE = source.L_SHIPMODE

WHEN NOT MATCHED THEN
    INSERT (
        L_ORDERKEY,
        L_PARTKEY,
        L_SUPPKEY,
        L_QUANTITY,
        L_EXTENDEDPRICE,
        L_DISCOUNT,
        L_TAX,
        L_RETURNFLAG,
        L_LINESTATUS,
        L_SHIPDATE,
        L_COMMITDATE,
        L_RECEIPTDATE,
        L_SHIPINSTRUCT,
        L_SHIPMODE
    )
    VALUES (
        source.L_ORDERKEY,
        source.L_PARTKEY,
        source.L_SUPPKEY,
        source.L_QUANTITY,
        source.L_EXTENDEDPRICE,
        source.L_DISCOUNT,
        source.L_TAX,
        source.L_RETURNFLAG,
        source.L_LINESTATUS,
        source.L_SHIPDATE,
        source.L_COMMITDATE,
        source.L_RECEIPTDATE,
        source.L_SHIPINSTRUCT,
        source.L_SHIPMODE
    );
