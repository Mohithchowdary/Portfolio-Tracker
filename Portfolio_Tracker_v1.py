import os, time, gspread, json
from datetime import datetime
from binance import Client
from kiteconnect import KiteConnect
from requests import Session

#load_apis
with open('core.json') as file: core = json.load(file)

#google_sheets
Call = gspread.service_account(filename="core.json")
File = Call.open('Portfolio_Tracker_v1.0')
ws = File.worksheet('v1.0')

#binance
api_key = core['binance_api_key']
api_secret = core['binance_api_secret']
client = Client(api_key, api_secret)
info = client.get_account()

#coinmarketcap
url = core['cmc_url']
cmc_api_key = core['CMC_PRO_API_KEY']

#zerodha
kite = KiteConnect(api_key= core['kite_api_key'])
kite.set_access_token(core['kite_access_token'])

class Portfolio_tracker_v1:
    #update_crypto_holdings
    def crypto():
        i=8    
        #fetch_holdings
        for asset_value in info['balances']:
            if float(asset_value['free']) > 0:   
                symbol_ = asset_value['asset']
                currency_ = 'INR'
            
                parameters = {'symbol': symbol_, 'convert': currency_}
                headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': cmc_api_key}

                session = Session()
                session.headers.update(headers)
                response = session.get(url, params=parameters)
                data = json.loads(response.text)

                
                try:
                    for item in data["data"].values():
                        for quote in item["quote"].items():
                            coin_name, coin_price = item["name"], quote[1]["price"]
                            try:
                                coin_change = str(round(quote[1]["percent_change_1h"],2))
                                ws.update('E' + str(i), coin_change + "%") #percentage_change_1h  
                            except:
                                ws.update('E' + str(i), 'N/A')
                except:
                    pass

                #update_serial_no
                ws.update('A' + str(i), str(i-7))
                
                #update_symbols_quantities
                ws.update('B' + str(i), str(coin_name))             #name
                ws.update('C' + str(i), asset_value['asset'])       #symbol
                ws.update('F' + str(i), str(asset_value['free']))   #quantity
                
                #update_current_holding_prices
                try:
                    ws.update('D' + str(i), round(coin_price,5))  
                    quantity_price = round((float(asset_value['free'])*coin_price),2)
                    ws.update('H' + str(i), quantity_price)
                          
                except:
                    ws.update('D' + str(i), 'N/A')
                    ws.update('H' + str(i), 'N/A')
                i+=1

    #update_stock_holdings
    def stocks():
        i=8
        for holding in kite.holdings():
            ws.update('K' + str(i), str(i-7))                   #serial_no    
            ws.update('M' + str(i), holding['tradingsymbol'])   #symbol
            ws.update('P' + str(i), holding['quantity'])        #quantity
            i+=1

#update_date_time
def last_updated():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.today().strftime('%Y-%m-%d')
    ws.update('H5', 'last_updated: ' + current_time)
    ws.update('A5', 'date: ' + current_date)

#update_loop
x = 0
while x!=-1:
    last_updated()
    os.system('cls')
    print('last_updated at', (str(datetime.today())))
    Portfolio_tracker_v1.crypto()
    Portfolio_tracker_v1.stocks()
    time.sleep(60) #updates_every_60_seconds
