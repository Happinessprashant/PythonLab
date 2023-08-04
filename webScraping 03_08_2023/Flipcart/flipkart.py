import requests
from bs4   import BeautifulSoup as bs
from urllib.request import urlopen as uReq #alias
import logging

flipcart_url="https://www.flipkart.com/search?q="+"iphone12pro"

#print Url 
print("flipcart_url==============================\n",flipcart_url)

# Url open
uReq(flipcart_url)
data_flipcart=uReq(flipcart_url)
