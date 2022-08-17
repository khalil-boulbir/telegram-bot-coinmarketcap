from unicodedata import name
import requests
import time
import pandas as pd
import numpy as np
# global variables
api_key = 'your api key'
bot_key = 'chat key'
chat_id = '1027866118'
limit = 0.3
limit_time = 5*60
listed=[]
name=[]

#def get_price():
url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
        'start' : '1',
        'limit' : '15',
        'convert': 'USD'
    }
headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
reponse = requests.get(url,headers=headers,params=parameters).json()
price_bitcoin = reponse['data'][0]['quote']['USD']['price']

data=reponse['data']
data=pd.DataFrame(data)
data=data.drop(["symbol","slug","cmc_rank" , "num_market_pairs" , "platform","self_reported_circulating_supply" ,"self_reported_market_cap" ,"circulating_supply","date_added","tags","total_supply","max_supply","last_updated"],axis=1)
for i in data['quote']:
        listed.append(i["USD"]["price"])
    
data['quote']=listed
print(data)
data=data[data["quote"]<limit]
msg=str(data)
url1 = "https://api.telegram.org/bot"+bot_key+"/sendMessage?chat_id="+chat_id+"&text="+ msg
requests.get(url1)
   # return price_bitcoin
#def send_updat(chat_id,bot_key,msg):
    
#def main():
     
#main()
