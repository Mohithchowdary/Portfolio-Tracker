#!python
import logging
from kiteconnect import KiteConnect

kite = KiteConnect(api_key="qkzaknavbf1e8pqn")
data = kite.generate_session("j6MElDAz6JN8e2DDdi7NImqi0As3a8CZ", api_secret="1kauc1u9k5sq81r2vz2psou21iyvd13x")
print(data["access_token"])