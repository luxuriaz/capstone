from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
ImageAddressList = []
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    ImageAddressList.append(image["src"])


for address in ImageAddressList:
    print (address)
    print (bsObj.find("img",{"src":address}).parent.previous_sibling.get_text())
