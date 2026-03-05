from .Settings import settings
import requests
import pandas as pd

class APICalls:

    def __init__(self):
        self.base_url = settings.base_url
        self.session = requests.Session()
        self.session.headers.update({'accept': 'application/json'})
        self.auth_params = {
            "key_name": settings.key_name, 
            "api_key": settings.api_key
        }

    def get_historyChart(self, start_date=None, end_date=None, limit=None):
        url = f"{self.base_url}/get_historyChart"
        params = {
            **self.auth_params,
            "start_date": start_date,
            "end_date": end_date,
            "limit": limit
        }
        response = self.session.get(url, params=params)
        print("response: ", response)
        df = pd.DataFrame(response.json())
        return df

    def get_liveChart(self, start_time=None, end_time=None, limit=None):
        url = f"{self.base_url}/get_liveChart"
        params = {
            **self.auth_params,
            "start_time": start_time,
            "end_time": end_time,
            "limit": limit
        }
        response = self.session.get(url, params=params)
        return pd.DataFrame(response.json())
    

    def get_historyOhlc(self, start_date=None, end_date=None, limit=None):
        url = f"{self.base_url}/get_historyOhlc"
        params = {
            **self.auth_params,
            "start_date": start_date,
            "end_date": end_date,
            "limit": limit
        }
        response = self.session.get(url, params=params)
        df = pd.DataFrame(response.json())
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df

    def get_liveOhlc(self, start_time=None, end_time=None, limit=None):
        url = f"{self.base_url}/get_liveOhlc"
        params = {
            **self.auth_params,
            "start_time": start_time,
            "end_time": end_time,
            "limit": limit
        }
        response = self.session.get(url, params=params)
        return pd.DataFrame(response.json())
    