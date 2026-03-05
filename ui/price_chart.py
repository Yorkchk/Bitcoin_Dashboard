import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render_bitcoin_chart(df, chart_type):
    # If the dataframe is empty, show a warning and return
    if df.empty:
        st.warning("No data available for the selected timeframe.")
        return

    fig = go.Figure()

    if chart_type == "Line":
        # Handle the price data format
        # Check if date column is 'bitcoin_date' (price sample) or 'timestamp' (OHLC sample)
        date_col = 'bitcoin_date' if 'bitcoin_date' in df.columns else 'timestamp'
        
        fig.add_trace(go.Scatter(
            x=df[date_col], 
            y=df['price'] if 'price' in df.columns else df['close'], 
            mode='lines', 
            line=dict(color='#F7931A', width=2),
            name="Bitcoin Price"
        ))
        
    else:
        # Handle the OHLC data format
        # Note: If you pass price data to the candlestick chart, it will 
        # need 'open', 'high', 'low', 'close' columns to exist in the df.
        fig.add_trace(go.Candlestick(
            x=df['timestamp'],
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            name="OHLC"
        ))

    fig.update_layout(
        template="plotly_dark",
        xaxis_rangeslider_visible=False,
        margin=dict(l=0, r=0, t=30, b=0),
        height=450,
        hovermode="x unified",
        yaxis_title="Price (USD)",
        # This makes the grid lines subtle for a cleaner look
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#333')
    )
    
    st.plotly_chart(fig, use_container_width=True)