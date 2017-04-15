from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
headers = {'User-agent': 'Mozilla/5.0'}
html = urlopen(input("enter the url: "))
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
