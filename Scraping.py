####### Web_scraping_Amazon ############
####### Author: Midhunkumar ############

#Importing required Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
#from requests_html import HTMLSession
import warnings
warnings.simplefilter("ignore")

HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3','Accept-Language': 'en-US, en;q=0.5'})

url = "http://www.amazon.in/dp/"

asin_array = pd.read_csv('mithunbro.csv') #
# Defining Empty list for price , Title and URL
URL_list = []
Tittle_list = []
Price_list = []

for i in asin_array["ASIN"]:
    sleep(4)
    URL= url + i
    #asin_array.append(URL)
    URL_list.append(URL)

    print("Procceing URL " + URL)
    page = requests.get(URL,headers=HEADERS) #getting the Html page
    soup = BeautifulSoup(page.content, features='lxml') # Using Beautiful soup for Web_scraping_Amazon

    #Getting Tittle
    tittle = soup.find(id='productTitle').get_text().strip()
    #asin_array.append(tittle)
    Tittle_list.append(tittle)

    #getting price
    try:
        price = float(soup.find(id='priceblock_ourprice').get_text().replace('₹', '').replace(',', '').strip())
    except:
        price = ''
    Price_list.append(price)
    #asin_array.append(price)

# Appending Coloums in Asin DataFrame
asin_array["URl"] = URL_list
asin_array["Tittle"] = Tittle_list
asin_array["Price"]  = Price_list

file_name = "New_List.xlsx"
asin_array.to_excel(file_name)

print("File successfully imported in Current Working Directory as " + file_name)
