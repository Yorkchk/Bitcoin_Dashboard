from Settings import settings
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

    #   'https://bitcoin-full-stackv3.graymushroom-f6c082ac.canadaeast.azurecontainerapps.io/get_historyChart?key_name=testv3&api_key=d2c4a40895b0481fa2ffeb478f981d59&start_date=2026-01-01&end_date=2026-01-05&limit=100' 
    def get_historyChart(self, start_date=None, end_date=None, limit=None):
        url = f"{self.base_url}/get_historyChart"
        params = {
            **self.auth_params,
            "start_date": start_date,
            "end_date": end_date,
            "limit": limit
        }
        response = self.session.get(url, params=params)
        return pd.DataFrame(response.json())
    
api_call1 = APICalls()
df = api_call1.get_historyChart(start_date="2026-01-01", end_date="2026-01-05", limit=100)
print(df.head())