#random choices and more
import random
#Needed to get the URL
import requests
#Important for webscraping
from bs4 import BeautifulSoup
#The Webside you want
url='https://www.finanzen.net/waehrungsrechner/us-dollar_euro'

A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )
 
Agent = A[random.randrange(len(A))]
 
headers = {'user-agent': Agent}
#get the Website from request
page = requests.get(url, headers=headers)

soup=BeautifulSoup(page.content,'lxml')

#Find the Dollar andEuro Price
second_display=soup.find(id="currency-second-display")
first_display=soup.find(id="currency-first-display")

#Print Them All
print(first_display)
print(second_display)
