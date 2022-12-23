import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://books.toscrape.com/').text
soup = BeautifulSoup(page, 'lxml')
file = open(r"code.html", "w")
# print("Writting...")
# print(soup.prettify())
# file.write(soup.prettify())
content = soup.find_all(class_='product_pod')
content = str(content)
re_title = r'title="(.*?)">'
title_list = re.findall(re_title, content)
re_prices = "£(.*?)</p>"
price_list = re.findall(re_prices, content)

with open("output.txt", "w") as f:
    for title, price, in zip(title_list, price_list):
        f.write(title+"\t"+price+"\n")
