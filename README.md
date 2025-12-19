# Aave Liquidation Risk — DeFi Data Product

**DeFi & on-chain intelligence for decision-makers**

This project is an end-to-end **DeFi data product** focused on **Aave liquidation risk**, built as both:
- a **company website prototype (WITIN)**, and  
- a **Data Engineer portfolio project** demonstrating real-world ETL, storage, and data delivery.

---

## Project Objective

To design and deploy a clean, automated data pipeline that:
- ingests **crypto market data** and **protocol-level metrics**,
- transforms and stores them in analytics-ready formats,
- serves insights through a **Streamlit web interface** suitable for non-technical decision-makers.

The long-term goal is to extend this product into a **full liquidation risk engine** based on real Aave positions and stress-test scenarios.

---

## Architecture (End-to-End)

APIs (Binance, DefiLlama)
↓
Ingestion (Python)
↓
Transform (Pandas)
↓
Storage (Parquet + DuckDB)
↓
Streamlit Web App

---

## Tech Stack

- **Language**: Python.  
- **Data ingestion**: REST APIs (Binance, DefiLlama).  
- **Data processing**: Pandas.  
- **Storage**: Parquet, DuckDB.  
- **Web app**: Streamlit.  
- **Version control**: Git & GitHub.  
- **Environment**: Virtualenv.  

---

## Repository Structure

aave_liquidation_risk_data_product/
│
├── app/ # Streamlit web app
│ ├── Home.py
│ ├── styles.py
│ └── pages/
│ ├── 1_Dashboards.py
│ ├── 2_Insights.py
│ ├── 3_Services.py
│ ├── 4_About.py
│ └── 5_Contact.py
│
├── pipelines/ # Data pipelines (ETL)
│ ├── ingest/
│ │ ├── binance_prices.py
│ │ └── defillama_aave.py
│ ├── transform/
│ │ └── marts.py
│ ├── utils/
│ │ └── io.py
│ └── run_etl.py
│
├── warehouse/ # Local data (ignored by Git)
│ ├── raw/
│ └── marts/
│
├── requirements.txt
├── .gitignore
└── README.md

---

## Data Pipeline Overview

### 1) Ingestion
- **Binance API**: spot prices (USDT proxy for USD).
- **DefiLlama API**: Aave protocol snapshot (TVL).

### 2) Transformation
- Schema normalization.
- Type casting & validation.
- Creation of analytics-ready marts:
  - `dim_prices`
  - `fact_protocol_snapshot`
  - `fact_risk_scenarios` (placeholder)

### 3) Storage
- Columnar storage using **Parquet**.
- Analytical database using **DuckDB**.

### 4) Serving
- Streamlit reads from Parquet/DuckDB.
- No direct API calls from the frontend.

---

## Deployment

The project is designed to be deployed on:

- Streamlit Community Cloud (recommended for portfolio & demo).

- Hugging Face Spaces.

- or containerized for cloud platforms (AWS / Fly.io / Render).

---

## Current Features

- Live market snapshot (Binance prices).

- Aave protocol overview (TVL).

- Clean KPI cards & dashboards.

- Modular ETL pipelines.

- Professional, minimalist UI (grey / dark theme).



