# readjson.py
# A program to read json data from the internet
# Author: David O'Connell

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
print("response type is ", type(response))
data = response.json()
print("data type is ", type(data))
print(data)
print("current price in Euros is ", end="")
print(data['bpi']['EUR']['rate_float'])