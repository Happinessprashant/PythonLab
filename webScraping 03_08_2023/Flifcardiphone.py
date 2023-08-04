
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

#url read 
# print("data",data_flipcart)
#store in variable
flipcart_page =data_flipcart.read()
data_flipcart.close()
print("data======================= \n",flipcart_page)

#apply BeautifulSoup Beauti for human readable data
soup = bs(flipcart_page, "html.parser")
print("Beauti-data \n ======================= \n",soup)


# get url links

bigbox = soup.find_all("div",{"class":"_1AtVbE col-12-12"})

#printall

print("Length of Big Box is ",len(bigbox))
# delete some data
del bigbox[0:2]
print("Length of Big Box is ",len(bigbox))
print("\n")

#link
productlink ="https://www.flipkart.com"+bigbox[0].div.div.div.a['href']

#request
product_req = requests.get(productlink)

#apply BeautifulSoup Beauti for human readable data
product_data = bs(product_req.text , "html.parser")

#print data for product
print("================\n request data \n ================\n ",product_data)

#find a tag 
commment_box = product_data.find_all("div",{"class":"_16PBlm"})

# length of comment box
print("================\n length of comment box \n ==================\n ",len(commment_box))
#print

# print("====================\n prod_data \n====================\n",commment_box)
# print("====================\n prod_data \n====================\n",commment_box[0].div.div.find_all('p', {"class":"_2sc7ZR _2V5EHH"})[0].text)

# print reviwer names
# for i in commment_box:
#     print(i.div.div.find_all('p', {"class":"_2sc7ZR _2V5EHH"})[0].text)

# print ratings

# for i in commment_box:
#     print(i.div.div.div.div.text)


#print header
# for i in commment_box:
#     print(i.div.div.div.p.text)


#print actual comments
for i in commment_box:
    print(i.div.div.find_all("div",{"class":""})[0].div.text ,"\n")





# for i in bigbox:
#     print("https://www.flipkart.com"+i.div.div.div.a['href']+"\n")


#
