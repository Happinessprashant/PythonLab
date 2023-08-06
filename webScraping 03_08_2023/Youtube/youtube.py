import requests
from bs4   import BeautifulSoup as bs
from urllib.request import urlopen as uReq #alias
import logging


youtube_url="https://www.youtube.com/results?search_query="+"HiteshChoudhary"
# youtube_url="https://www.youtube.com/"+"@HiteshChoudharydotcom"

print("=========\n url ===========\n",youtube_url)

#url open
uReq(youtube_url)
data_youtube=uReq(youtube_url)

youtube_page =data_youtube.read()
# data_youtube.close()

print("=====================\nyoutube_page\n======================= \n",youtube_page)


#apply BeautifulSoup Beauti for human readable data
youtube_html = bs(youtube_page, "html.parser")
print("\n Beauti-data \n ======================= \n",youtube_html)

# get url links

# bigbox = youtube_page.find("body",{"dir":"ltr"})

#printall


# print("Length of Big Box is ",len(bigbox) ,"\n")
# # delete some data

# print(" \n Data of Big Box is \n ",(bigbox))







