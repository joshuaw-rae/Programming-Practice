# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/currencies/bitcoin/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "lxml")
div = soup.find("div", {"class" : "col-xs-6 col-sm-8 col-md-4 text-left"}).find("span", {"class" : "text-large2"})

for i in div:
    print (i)