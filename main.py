import streamlit as st
from ui.price_chart import render_bitcoin_chart
from ui.stats_cards import render_stats_cards
from data.api_calls import APICalls
from datetime import datetime, timedelta

api_call = APICalls()


# Set page to Dark Mode by default
st.set_page_config(
    page_title="Bitcoin Analytics Pro",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for "Flash Card" styling
st.markdown("""
    <style>
    div[data-testid="stMetric"] {
        background-color: #1E1E1E;
        border: 1px solid #333;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("₿ Bitcoin Market Overview")

    # --- TOP SECTION: CONTROLS ---
    col_type, col_gran = st.columns([1, 2])
    
    with col_type:
        chart_type = st.segmented_control(
            "Chart Type", 
            options=["Line", "Candlestick"], 
            default="Line"
        )
    
    with col_gran:
        granularity = st.segmented_control(
            "Timeframe", 
            options=["1D", "1W", "1M", "3M", "All"], 
            default="1D"
        )
    days = {
        "1W": 7,
        "1M": 30,
        "3M": 90,
        "All": None
    }

    # --- MIDDLE SECTION: THE GRAPH ---
    # In a real app, you'd fetch data based on 'granularity' here
    end_date = start_date = None
    if granularity != "1D" and granularity != "All":
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days[granularity]) if days[granularity] else None

        start_date = start_date.strftime("%Y-%m-%d") if start_date else None
        end_date = end_date.strftime("%Y-%m-%d")

    if chart_type == "Line":
        if granularity == "1D":
            bitcoin_data = api_call.get_liveChart()
            render_bitcoin_chart(bitcoin_data, chart_type)
        else:
            bitcoin_data = api_call.get_historyChart(start_date=start_date, end_date=end_date)
            render_bitcoin_chart(bitcoin_data, chart_type)
    else:
        if granularity == "1D":
            ohlc_data = api_call.get_liveOhlc()
            render_bitcoin_chart(ohlc_data, chart_type)
        else:
            ohlc_data = api_call.get_historyOhlc(start_date=start_date, end_date=end_date)
            render_bitcoin_chart(ohlc_data, chart_type)

    st.divider()

    # --- BOTTOM SECTION: FLASH CARDS ---
    st.subheader("Market Statistics")
    render_stats_cards()

if __name__ == "__main__":
    main()