import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="WITIN", layout="wide")

ROOT = Path(__file__).resolve().parents[1]
PRICES = ROOT / "warehouse" / "marts" / "dim_prices.parquet"
AAVE = ROOT / "warehouse" / "marts" / "fact_protocol_snapshot.parquet"
RISK = ROOT / "warehouse" / "marts" / "fact_risk_scenarios.parquet"

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

st.title("DeFi & On-chain intelligence for decision-makers")
st.caption("Aave liquidation risk — built as an end-to-end data product (ETL → storage → refresh → dashboards).")

if PRICES.exists() and AAVE.exists() and RISK.exists():
    prices = pd.read_parquet(PRICES)
    aave = pd.read_parquet(AAVE)
    risk = pd.read_parquet(RISK)

    last_refresh = safe_last_refresh(prices, aave, risk)
    if last_refresh == "N/A":
        st.warning("Data loaded but timestamps are missing. Re-run ETL: `python -m pipelines.run_etl`")
    else:
        st.success(f"Data ready • Last refresh (UTC): {last_refresh}")

    c1, c2, c3 = st.columns(3)

    try:
        tvl = float(aave["tvl_usd"].iloc[0])
        c1.metric("Aave TVL (USD)", f"{tvl:,.0f}")
    except Exception:
        c1.metric("Aave TVL (USD)", "N/A")

    eth_row = prices[prices.get("asset_symbol", pd.Series(dtype=str)) == "ETH"] if not prices.empty else prices
    if not eth_row.empty and "price_usd" in eth_row.columns:
        try:
            c2.metric("ETH price (USDT≈USD)", f"{float(eth_row['price_usd'].iloc[0]):,.2f}")
        except Exception:
            c2.metric("ETH price (USDT≈USD)", "N/A")
    else:
        c2.metric("ETH price (USDT≈USD)", "N/A")

    c3.metric("Risk scenarios", f"{len(risk)}")

    st.divider()
    left, right = st.columns(2)
    with left:
        st.subheader("Market snapshot (Binance)")
        st.dataframe(prices, use_container_width=True)
    with right:
        st.subheader("Aave snapshot (DefiLlama)")
        st.dataframe(aave, use_container_width=True)

else:
    st.warning("Chưa có data marts. Chạy ETL: `python -m pipelines.run_etl`")

st.divider()
st.markdown("📩 **Request a briefing:** [Huyen Tran](mailto:huyentr246@gmail.com)")
