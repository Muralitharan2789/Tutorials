# Run this cell to load the necessary python libraries
from requests import get
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import numpy as np  
import re 
import pickle


# Write your code below
html =  get('https://coinmarketcap.com/')  #parse the webpage
html_soup =  BeautifulSoup(html.text, 'html.parser') #Convert the parsed page into beautifulsoup object

# Write your code below to obtain all 'tr' elements
###Start code here
crypto_containers =html_soup.find_all('tr')

# Lists to store the scraped data in
rank = []                    #List for rank of the currency (first column in the webpage)
currency_name = []           #List for name of the currency
market_cap = []              #List for market cap
price = []                   #List for price of the crypto currency
volume = []                  #List for Volume(24h)
supply = []                  #List for Circulating supply
change = []                  #List for Change(24h)
#crypto_containers=crypto_containers[3:]
for i in range(len(crypto_containers)):
    try:
        if crypto_containers[i].find_all('td')[0].text:
            rank.append(int(crypto_containers[i].find_all('td')[0].text))
        #rank.append(crypto_containers[i].find_all('td')[0].text)
        currency_name.append(crypto_containers[i].find_all('td')[1].text.split()[1])
        market_cap.append(crypto_containers[i].find_all('td')[2].text)
        price.append(crypto_containers[i].find_all('td')[3].text)
        volume.append(crypto_containers[i].find_all('td')[4].text)
        supply.append(crypto_containers[i].find_all('td')[5].text)
        change.append(crypto_containers[i].find_all('td')[6].text)
    except:
        continue
    
    
'''     rank.append(int(crypto_containers[i].find_all('td')[0].text))
        currency_name.append(crypto_containers[i].find_all('td')[1].text)
        market_cap.append(int(''.join(re.findall('\d+',crypto_containers[i].find_all('td')[2].text))))
        price.append(float(''.join(re.findall('\d+\.?',crypto_containers[i].find_all('td')[3].text))))
    except:
        continue
 '''  
 
crypto_df = pd.DataFrame({
                         'rank' : rank,
                         'currency_name' : currency_name,
                         'market_cap' : market_cap,
                         'price' : price,
                         'volume' : volume,
                         'supply' : supply,
                         'change' : change
                         })
    
crypto_df['market_cap']=crypto_df['market_cap'].apply(lambda x: int(''.join(re.findall('\d+',x))))
crypto_df['price']=crypto_df['price'].apply(lambda x: float(''.join(re.findall('\d+\.?',x))))
crypto_df['volume']=crypto_df['volume'].apply(lambda x: int(''.join(re.findall('\d+',x))))
crypto_df['supply']=crypto_df['supply'].apply(lambda x: int(''.join(re.findall('\d+',x))))
crypto_df['change']=crypto_df['change'].apply(lambda x: float(x.split('%')[0]))