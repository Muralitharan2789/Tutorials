import requests
from bs4 import BeautifulSoup
import pandas as pd


Month=[]
Day=[]
Year=[]
Date=[]
Average_temperature=[]
Average_humidity=[]
Average_dewpoint=[]
Average_barometer=[]
Average_windspeed=[]
Average_gustspeed=[]
Average_direction=[]
Rainfall_for_month=[]
Rainfall_for_year=[]
Maximum_rain_per_minute=[]
Maximum_temperature=[]
Minimum_temperature=[]
Maximum_humidity=[]
Minimum_humidity=[]
Maximum_pressure=[]
Minimum_pressure=[]
Maximum_windspeed=[]
Maximum_gust_speed=[]
Maximum_heat_index=[]
for i in range(2009,2019):
    print(i)
    for j in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        print(j)
        url='http://www.estesparkweather.net/archive_reports.php?date='+str(i)+j
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')       
        results_table=soup.find_all('table',attrs={'border':"0", 'cellpadding':"3" ,'cellspacing':"0"})
        #results_table_top = results_table.find_all('tr', attrs={'class': 'table-top'})
        
        for k in range(len(results_table)-2):
            #Year.append(i)
            #Month.append(results_table[k].text.split()[0])
            #Day.append(results_table[k].text.split()[1])  
            Day=results_table[k].text.split()[1]
            Date.append(str(i)+'-'+str(j)+'-'+Day)
            #for l in range(len(results_cells)):
            #Month.append(results_table[k].text.split()[0])
            #Day.append(results_table[k].text.split()[1])
            results_cells = results_table[k].find_all('tr', attrs={'class': ['column-dark','column-light']})
            Average_temperature.append(results_cells[0].find_all('td')[1].text.split()[0])
            Average_humidity.append(results_cells[1].find_all('td')[1].text.split()[0])
            Average_dewpoint.append(results_cells[2].find_all('td')[1].text.split()[0])
            Average_barometer.append(results_cells[3].find_all('td')[1].text.split()[0])
            Average_windspeed.append(results_cells[4].find_all('td')[1].text.split()[0])
            Average_gustspeed.append(results_cells[5].find_all('td')[1].text.split()[0])
            Average_direction.append(results_cells[6].find_all('td')[1].text.split()[0])
            Rainfall_for_month.append(results_cells[7].find_all('td')[1].text.split()[0])
            Rainfall_for_year.append(results_cells[8].find_all('td')[1].text.split()[0])
            Maximum_rain_per_minute.append(results_cells[9].find_all('td')[1].text.split()[0])
            Maximum_temperature.append(results_cells[10].find_all('td')[1].text.split()[0])
            Minimum_temperature.append(results_cells[11].find_all('td')[1].text.split()[0])
            Maximum_humidity.append(results_cells[12].find_all('td')[1].text.split()[0])
            Minimum_humidity.append(results_cells[13].find_all('td')[1].text.split()[0])
            Maximum_pressure.append(results_cells[14].find_all('td')[1].text.split()[0])
            Minimum_pressure.append(results_cells[15].find_all('td')[1].text.split()[0])
            Maximum_windspeed.append(results_cells[16].find_all('td')[1].text.split()[0])
            Maximum_gust_speed.append(results_cells[17].find_all('td')[1].text.split()[0])
            Maximum_heat_index.append(results_cells[18].find_all('td')[1].text.split()[0])


'''    if i == 2018 and j == '10':
        break'''



df=pd.DataFrame(list(zip(Date,Average_temperature,Average_humidity,Average_dewpoint,Average_barometer,Average_windspeed,Average_gustspeed,Average_direction,Rainfall_for_month,Rainfall_for_year,Maximum_rain_per_minute,Maximum_temperature,Minimum_temperature,Maximum_humidity,Minimum_humidity,Maximum_pressure,Minimum_pressure,Maximum_windspeed,Maximum_gust_speed,Maximum_heat_index)),
             columns=['Date','Average temperature (°F)', 'Average humidity (%)',
                      'Average dewpoint (°F)', 'Average barometer (in)',
                      'Average windspeed (mph)', 'Average gustspeed (mph)',
                      'Average direction (°deg)', 'Rainfall for month (in)',
                      'Rainfall for year (in)', 'Maximum rain per minute',
                      'Maximum temperature (°F)', 'Minimum temperature (°F)',
                      'Maximum humidity (%)', 'Minimum humidity (%)', 'Maximum pressure',
                      'Minimum pressure', 'Maximum windspeed (mph)',
                      'Maximum gust speed (mph)', 'Maximum heat index (°F)'])

    
df=df[~df['Date'].str.contains('and')]
df['Date']=pd.to_datetime(df['Date'])
df=df.set_index('Date')


import re
def floating(x):
    return float(re.findall(r"[-+]?\d*\.\d+|\d+", x)[0])


for i in list(df.columns):
    df[i]=df[i].apply(lambda x: floating(x))


df=df['2009-01-01':'2018-10-28']
df.to_csv('data_Weather.csv',index=False)
    
