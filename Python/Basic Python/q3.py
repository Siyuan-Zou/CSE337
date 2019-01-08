from bs4 import BeautifulSoup
import urllib.request

url = "https://finance.yahoo.com/commodities"
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')
symbols = soup.findAll('td', 'data-col0 Ta(start) Pstart(6px)')
symbols_Arr = list()
for x in symbols:
    symbols_Arr.append(str(x).split('"')[9])
#print(symbols_Arr)

names = soup.findAll('td', 'data-col1 Ta(start) Pend(10px)')
names_Arr = list()
for x in names:
    names_Arr.append(str(x).split(">")[1].split("<")[0])
#print(names_Arr)

last_prices = soup.findAll('td', 'data-col2 Ta(end) Pstart(20px)')
last_prices_Arr = list()
for x in last_prices:
    last_prices_Arr.append(str(x).split(">")[1].split("<")[0])
#print(last_prices_Arr)

market_times = soup.findAll('td', 'data-col3 Ta(end) Pstart(20px)')
market_times_Arr = list()
for x in market_times:
    market_times_Arr.append(str(x).split(">")[1].split("<")[0])
#print(market_times_Arr)

changes = soup.findAll('td', 'data-col4 Ta(end) Pstart(20px)')
changes_Arr = list()
for x in changes:
    changes_Arr.append(str(x).split(">")[2].split("<")[0])
#print(changes_Arr)

percent_changes = soup.findAll('td', 'data-col5 Ta(end) Pstart(20px)')
percent_changes_Arr = list()
for x in percent_changes:
    percent_changes_Arr.append(str(x).split(">")[2].split("<")[0])
#print(percent_changes_Arr)

#List of List
commodities_Arr = [symbols_Arr, names_Arr, last_prices_Arr, market_times_Arr, changes_Arr, percent_changes_Arr]
#print(commodities_Arr)

f = open("commodities.txt", "w")
for i in range(len(symbols_Arr)):
    f.write(symbols_Arr[i] + ", " +
            names_Arr[i] + ", " +
            last_prices_Arr[i] + ", " +
            market_times_Arr[i] + ", " +
            changes_Arr[i] + ", " +
            percent_changes_Arr[i]+'\n')
f.close()
