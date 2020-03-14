import requests
from bs4 import BeautifulSoup
search = input("Search Something on EBAY: ")
URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={}&_sacat=0".format(search)
content = requests.get(URL).text
soup = BeautifulSoup(content, "html.parser")
# data = soup.find(class_ = "srp-results srp-list clearfix").find_all(class_='s-item')
info = soup.find_all(class_ = "s-item__price")
for price in info:
    price = price.get_text()
    if "to" not in price:
        print(price[1: len(price)-1])