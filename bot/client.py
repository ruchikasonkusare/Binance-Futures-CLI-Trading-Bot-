import time
import hmac
import hashlib
import requests
import os
from urllib.parse import urlencode
from dotenv import load_dotenv
import logging

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"

class BinanceFutureCLients:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret_key = os.getenv("BINANCE_SECRET_KEY")
        

    def sign(self,params:dict):
        query_string = urlencode(params)
        return hmac.new(
            self.secret_key.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        
    def place_order(self,params:dict):
        try:
            params['timestamp']=int(time.time()*1000)
            params['signature']=self.sign(params)

            headers = {"X-MBX-APIKEY": self.api_key}
            
            logging.info(f"Request Params :{params}")
            
            response=requests.post(
                BASE_URL+"/fapi/v1/order",
                headers=headers,
                params=params,
                timeout=10
            )        
            # response.raise_for_status()
            data = response.json()
            if response.status_code != 200:
                print(f"Error Code: {data.get('code')}")
                print(f"Error Message: {data.get('msg')}")
                return data
            else:
                return data
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Network/API Error: {e}")
            raise
        
    