-- =========================================================
-- Retail Data Engineering Pipeline
-- Business / Analytical Queries
-- =========================================================


-- 1. Customers with low account balance
SELECT
    C_NAME,
    C_ACCTBAL
FROM customers
WHERE C_ACCTBAL < 1000
ORDER BY C_ACCTBAL DESC;


-- 2. Orders grouped by order status
SELECT
    O_ORDERSTATUS,
    COUNT(*) AS order_count
FROM orders
GROUP BY O_ORDERSTATUS
ORDER BY order_count DESC;


-- 3. Top 5 most expensive parts
SELECT TOP 5
    P_NAME,
    P_RETAILPRICE
FROM parts_info
ORDER BY P_RETAILPRICE DESC;


-- 4. Orders with delayed shipment
SELECT
    O_ORDERKEY,
    L_SHIPDATE,
    L_RECEIPTDATE
FROM orders
JOIN lineitem
    ON orders.O_ORDERKEY = lineitem.L_ORDERKEY
WHERE L_RECEIPTDATE > L_SHIPDATE;


-- 5. Customers who placed orders during 1992
SELECT DISTINCT
    C_NAME
FROM customers
JOIN orders
    ON customers.C_CUSTKEY = orders.O_CUSTKEY
WHERE O_ORDERDATE >= '1992-01-01'
  AND O_ORDERDATE < '1993-01-01';
