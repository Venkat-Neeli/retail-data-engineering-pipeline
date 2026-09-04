# Retail Data Engineering Pipeline

An end-to-end data engineering project built using Azure Data Lake Storage, Azure Databricks, PySpark, Delta Lake, Azure Synapse Analytics, and Power BI.

## Architecture

![Retail Data Engineering Pipeline](architecture/architecture-diagram.png)

## Technologies

| Category | Technology |
|---|---|
| Cloud | Microsoft Azure |
| Data Lake | Azure Data Lake Storage |
| Processing | Azure Databricks |
| Programming | Python, PySpark |
| Storage Format | Parquet, Delta Lake |
| Data Warehouse | Azure Synapse Analytics |
| Analytics | SQL |
| Visualization | Power BI |
| Security | Azure Key Vault |

## Project Overview

This project demonstrates an end-to-end retail data engineering pipeline.

Retail datasets are ingested into Azure Data Lake Storage and processed using Azure Databricks and PySpark. The data is organized using a Medallion Architecture with Bronze, Silver, and Gold layers.

The Silver layer contains cleaned and enriched Delta tables, while the Gold layer contains analytics-ready datasets. The processed data is then made available through Azure Synapse Analytics for SQL-based analysis and Power BI for business reporting.

### Pipeline Flow

Source Data
→ Azure Data Lake Storage
→ Bronze Layer
→ Databricks / PySpark
→ Silver Layer
→ Delta Lake
→ Gold Layer
→ Azure Synapse Analytics
→ Power BI

## Data Architecture

### Bronze Layer

The Bronze layer stores the ingested source data with minimal transformation.

- Raw retail datasets
- Original source structure
- Initial ingestion and storage
- Supports auditability and reprocessing

### Silver Layer

The Silver layer contains cleaned, standardized, and enriched data.

- Null and duplicate handling
- String standardization
- Date transformations
- Data enrichment using joins
- Derived columns and business calculations
- Delta Lake tables
- Schema enforcement
- MERGE / UPSERT operations

### Gold Layer

The Gold layer contains analytics-ready datasets.

- Business-ready data
- Aggregated and transformed datasets
- Optimized for analytical queries
- Consumed by Azure Synapse Analytics and Power BI

## Datasets

The pipeline processes the following retail datasets:

| Dataset | Description |
|---|---|
| Customers | Customer information and account details |
| Orders | Customer orders and order-level information |
| Lineitem | Individual items within each order |
| Part | Product/part information |
| Partsupp | Supplier and product relationship |
| Supplier | Supplier information |
| Nation | Nation reference data |
| Region | Region reference data |

### Data Relationships

The datasets are connected through keys such as:

- Customer → Orders
- Orders → Lineitem
- Part → Lineitem
- Supplier → Lineitem
- Part → Partsupp
- Supplier → Partsupp
- Nation → Customer
- Nation → Supplier
- Region → Nation

## Key Engineering Concepts

### PySpark

- DataFrame operations
- Filtering
- Joins
- Aggregations
- Window functions
- Column transformations
- Date transformations
- String transformations

### Delta Lake

- Delta tables
- Schema enforcement
- Schema management
- MERGE / UPSERT operations

### Data Engineering

- ETL pipeline development
- Medallion Architecture
- Data quality validation
- Data cleansing
- Data enrichment
- Partitioned data storage
- Analytics-ready data modeling

### Azure

- Azure Data Lake Storage
- Azure Databricks
- Azure Synapse Analytics
- Azure Key Vault

### Analytics

- SQL analytical queries
- Power BI dashboards
- Business reporting

