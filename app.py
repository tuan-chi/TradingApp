"""
create function connect website

1. connect
2. show information
3. extracting data to json

"""
import json
from datetime import date
from bs4 import BeautifulSoup
from urllib.request import urlopen
from stock import Sock

url = urlopen('https://finance.yahoo.com/trending-tickers')

# url connect address website
bsObj = BeautifulSoup(url, 'html.parser')
y_finance = bsObj.find('table', attrs={'class': 'yfinlist-table'})
y_finance_data = y_finance.tbody


data = []
symbol = ''
name = ''
# append each name stock markets into data
for element in y_finance_data:
    try:
        symbol = element.find(attrs={'class': 'data-col0'}).text
        name = element.find(attrs={'class': 'data-col1'}).text
    except:
        print('Error')
    sock = Sock(name, symbol)
    data.append(sock)


# extracting data to json
with open('{}.json'.format(date.today()), 'w') as json_file:
    with open('socks.json', 'r') as json_sock:
        date = {}
        date = []
        for title in data:
            date.append(title.serialize())
            json.dump(date, json_file, indent=2)