# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd

records = []
for j in range(2000,2021):
    j=str(j)
    for i in range(1,13):
        i=str(i)
        r = requests.get('https://www.livechennai.com/get_goldrate_history.asp?monthno='+i+'&yearno='+j)
        soup = BeautifulSoup(r.text, 'html.parser')
        results = soup.find_all('tr', attrs={'class':'dark'})
        for result in results:
            date=result.contents[1].text[3:]
            price=result.contents[5].text
            records.append((date, price))

df = pd.DataFrame(records, columns=['day', 'price'])
for i in range(df.shape[0]):
    try:
        df['price']=df['price'].apply(lambda x: int(x.split('.')[0]))
    except:
        df['price']=df['price'].apply(lambda x: ''.join(x.split('.')[0].split(',')))
    else:
        break
df['day'] = pd.to_datetime(df['day'])
df['year'] = df['day'].apply(lambda x: x.year)
df['month'] = df['day'].apply(lambda x: x.month)
df['date'] = df['day'].apply(lambda x: x.day)
df.to_csv('gold_price_2006_20.csv', index=False, encoding='utf-8')

