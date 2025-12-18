import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Dashboards — WITIN", layout="wide")

ROOT = Path(__file__).resolve().parents[2]
PRICES = ROOT / "warehouse" / "marts" / "dim_prices.parquet"
RISK = ROOT / "warehouse" / "marts" / "fact_risk_scenarios.parquet"
AAVE = ROOT / "warehouse" / "marts" / "fact_protocol_snapshot.parquet"

def safe_last_refresh(*dfs) -> str:
    candidates = []
    for df in dfs:
        if df is None or df.empty or "ts_utc" not in df.columns:
            continue
        ts = pd.to_datetime(df["ts_utc"], errors="coerce", utc=True)
        ts = ts.dropna()
        if not ts.empty:
            candidates.append(ts.max())
    if not candidates:
        return "N/A"
    return max(candidates).isoformat()

st.title("Aave Liquidation Risk Dashboard")
st.caption("MVP dashboard.")

if not (PRICES.exists() and RISK.exists() and AAVE.exists()):
    st.warning("ETL: `python -m pipelines.run_etl`")
    st.stop()

prices = pd.read_parquet(PRICES)
risk = pd.read_parquet(RISK)
aave = pd.read_parquet(AAVE)

last_refresh = safe_last_refresh(prices, risk, aave)
st.info(f"Last refresh (UTC): {last_refresh}")

c1, c2 = st.columns(2)
with c1:
    st.subheader("Prices (USDT≈USD)")
    if prices.empty or "asset_symbol" not in prices.columns or "price_usd" not in prices.columns:
        st.warning("No price data. Re-run ETL.")
    else:
        st.bar_chart(prices.set_index("asset_symbol")["price_usd"])

with c2:
    st.subheader("Stress scenarios (placeholder)")
    st.dataframe(risk, use_container_width=True)

st.divider()
st.subheader("Aave protocol snapshot")
st.dataframe(aave, use_container_width=True)
