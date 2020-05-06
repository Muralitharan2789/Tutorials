# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:38:26 2020

@author: 529901
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


n=int(input('No of pages to be extracted:'))
records = []
for i in range(n):
    try:
        url='https://courses.analyticsvidhya.com/collections?category=free&page='+str(i)
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        results = soup.find_all('a', attrs={'class':'course-card course-card__public published'})
        for result in results:
            Name=result.find('h3').text
            URL='https://courses.analyticsvidhya.com'+result['href']
            Price=result.find('span',attrs={'class':'course-card__price'}).text
            try:
                Resources=result.find('span',attrs={'class':'course-card__bundle-size'}).text[:2]
            except:
                Resources=result.find('span',attrs={'class':'course-card__lesson-count'}).text[:2]
            records.append((Name, Price,Resources,URL))
    except:
        break
df = pd.DataFrame(records, columns=['Name','Price','Resources','URL'])
AV_FreeCourses=df[df['Price']=='Free']
AV_FreeCourses.to_csv('AV_FreeCourses.csv', index=False, encoding='utf-8')