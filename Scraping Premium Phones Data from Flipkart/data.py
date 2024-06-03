import pandas as pd
from bs4 import BeautifulSoup
import requests
Product_Names = []
Prices = []
Description = []
Ratings = []

for i in range(2,6):
    url = "https://www.flipkart.com/search?q=premium+phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.price_range.from%3D30000&p%5B%5D=facets.price_range.to%3DMax&page="+str(i)
    html_file = requests.get(url)
    soup = BeautifulSoup(html_file.text,'lxml')

    box=soup.find("div",class_="DOjaWF gdgoEp")
    names = box.find_all("div",class_="KzDlHZ")
    for i in names:
        name = i.text
        Product_Names.append(name)

    prices = box.find_all("div",class_="Nx9bqj _4b5DiR")
    for i in prices:
        name = i.text
        Prices.append(name)

    desc = box.find_all("ul",class_="G4BRas")
    for i in desc:
        name = i.text
        Description.append(name)

    rate = box.find_all("div",class_="XQDdHH")
    for i in rate:
        name = i.text
        Ratings.append(name)


max_len = max(len(Product_Names), len(Prices), len(Description), len(Ratings))

max_len = max(len(Product_Names), len(Prices), len(Description), len(Ratings))

Product_Names += [None] * (max_len - len(Product_Names))
Prices += [None] * (max_len - len(Prices))
Description += [None] * (max_len - len(Description))
Ratings += [None] * (max_len - len(Ratings))


df=pd.DataFrame({"Product Name":Product_Names,"Prices":Prices,"Description":Description,"Ratings":Ratings})

df.to_csv("premium_phones_flipkart.csv")

