import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)
Soup = BeautifulSoup(page.text, 'html')
print(Soup.prettify)

table = Soup.find('table', class_ = "wikitable sortable")
print(table)

Table_Column_names = table.find_all('th')
print(Table_Column_names)


Table_Column = [title_name.text.strip() for title_name in Table_Column_names]
print(Table_Column)

dataframe = pd.DataFrame(columns = Table_Column)
print (dataframe)

Companies_Data = table.find_all('tr')
print (Companies_Data)

for row in Companies_Data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip () for data in row_data]
    dataframe.loc[len(dataframe)] = individual_row_data

print (dataframe)


dataframe.to_csv('Top 100 companies in US by revenue.csv', index=False)


