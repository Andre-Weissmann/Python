## Amazon Web Scraping project

from bs4 import BeautifulSoup
import csv
import datetime
import requests
import time
import datetime

# Connect to website
URL = 'https://www.amazon.com/Data-Whisperer-Funny-Science-Software/dp/B07L85PM3K/ref=sr_1_12?crid=2R5VGBV21ZGEQ&keywords=data%2Banalyst%2Btshirt&qid=1681058736&sprefix=data%2Banalyst%2Btshirt%2Caps%2C2164&sr=8-12'

headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

# Gathering content from the website page
soup1 = BeautifulSoup(page.content, "html.parser") # raw website html format

soup2 = BeautifulSoup(soup1.prettify(), "html.parser") # refined website html format
 
# Specifying data in html to be gathered
title = soup2.find(id='productTitle').get_text()

price = soup2.find(class_='a-offscreen').get_text() 

print(title)
print(price)

# Cleaning / trimming the data price variable. Also removing $ symbol from price. Numeric value only = goal
price = price.strip()[1:]

# Cleaning / trimming the data for title variable.
title = title.strip()

print(title)
print(price)

# Date / Time stamps
today = datetime.date.today()

print(today)

# Creating headers for csv
header = ['Title', 'Price', 'Date']
data = [title, price, today]  # Creating a list of the data that was acquired from the website


# Writing (w) to a csv with spaces / newline to Windows OS
with open('AmazonScrapingDataset.csv','w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

import pandas as pd

# Dataframe (df) that will read information into csv located in a particular location in file explorer
df = pd.read_csv(r'C:\Users\nfsfa\AmazonScrapingDataset.csv')
print(df)

# Appending (a+) data to the csv file

with open('AmazonScrapingDataset.csv','a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

# Creating a function to automate the web scraping process
def check_price():
    URL = 'https://www.amazon.com/Data-Whisperer-Funny-Science-Software/dp/B07L85PM3K/ref=sr_1_12?crid=2R5VGBV21ZGEQ&keywords=data%2Banalyst%2Btshirt&qid=1681058736&sprefix=data%2Banalyst%2Btshirt%2Caps%2C2164&sr=8-12'

    headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    # Gathering content from the website page
    soup1 = BeautifulSoup(page.content, "html.parser") # raw website html format

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser") # refined website html format
 
    # Specifying data in html to be gathered
    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(class_='a-offscreen').get_text() 
    
    # Cleaning / trimming the data price variable. Also removing $ symbol from price. Numeric value only = goal
    price = price.strip()[1:]

    # Cleaning / trimming the data for title variable.
    title = title.strip()  
    
    import datetime
    
    # Date / Time stamps
    today = datetime.date.today()
    
    import csv 

    # Creating headers for csv
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]  # Creating a list of the data that was acquired from the website
    
    # Appending data
    with open('AmazonScrapingDataset.csv','a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
#Initializing a timer to gather data. Ex.) Every five seconds

while(True):
    check_price()
    time.sleep(5)

