# Importing Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
# loading a HTML document from web-page
r = requests.get('http://scrape-table.surge.sh/')
# Parsing the HTML using Beautiful Soup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('tr')
records = []
for result in results:
    #result=result.text
    #result=result.split('\n')
    result=[i for i in result.text.split('\n') if i]
    records.append(result)

df = pd.DataFrame(records)
df.columns=df.iloc[0]
df = df[1:]
df.to_csv('data.csv', index=False, encoding='utf-8')