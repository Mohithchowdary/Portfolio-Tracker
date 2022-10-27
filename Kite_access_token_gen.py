#!python
import logging
from kiteconnect import KiteConnect

kite = KiteConnect(api_key="your_api_key_here")
data = kite.generate_session("auth_key_here", api_secret="your_api_secret_here")
print(data["access_token"])
