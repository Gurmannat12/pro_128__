from turtle import distance
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv


START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page_source = requests.get(START_URL)
soup = bs(page_source.text,'html.parser')
star_table = soup.find_all('table')

temp_list= []
table_rows = star_table[7].find_all('tr')

for tr_tag in table_rows:
    td_tags = tr_tag.find_all('td')
    row = [i.text.rstrip() for i in td_tags]
    temp_list.append(row)

star_names = []
dist = []
mass = []
radius = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][0])
    dist.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(star_names, dist, mass, radius)), columns = ['Star_name', 'Distance', 'Mass', 'Radius'])
df2.to_csv("star.csv")