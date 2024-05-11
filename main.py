import requests
import json
import matplotlib.pyplot as plt

try:
    start_date = '20230101'
    end_date = '20230131'
    

    url = f'https://economia.awesomeapi.com.br/json/daily/BTC-BRL/31?start_date={start_date}&end_date={end_date}'
    
    btc_quotes = requests.get(url)
    
    if btc_quotes.status_code == 200:
        btc_quotes_dict = btc_quotes.json()
        
        btc_quotes_list = [float(item['bid']) for item in btc_quotes_dict]
        
        print(btc_quotes_list)
        
        plt.figure(figsize=(10, 6))
        plt.plot(btc_quotes_list, marker='o', linestyle='-', color='b', label='BTC-BRL')
        plt.title('Bitcoin Quotes (BTC-BRL) - January 2023')
        plt.xlabel('Days')
        plt.ylabel('Bid Price (BRL)')
        plt.grid(True)
        plt.legend()
        plt.show()
        
    else:
        print(f"Error fetching data: {btc_quotes.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Connection error: {e}")
