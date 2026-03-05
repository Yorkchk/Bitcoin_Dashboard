import streamlit as st

def render_stats_cards():
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Current Price", value="$108,452", delta="2.5%")
    with col2:
        st.metric(label="24h Volume", value="$35.2B", delta="-1.2%")
    with col3:
        st.metric(label="Market Cap", value="$2.1T", delta="0.8%")
    with col4:
        st.metric(label="Fear & Greed Index", value="72", delta="Greed")