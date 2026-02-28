import streamlit as st


class Settings:
    def __init__(self):
        self.base_url = st.secrets["BASE_URL"]
        self.key_name = st.secrets["KEY_NAME"]
        self.api_key = st.secrets["API_KEY"]

settings = Settings()