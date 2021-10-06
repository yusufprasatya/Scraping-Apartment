from bs4 import BeautifulSoup
import requests
from csv import writer

number = 26
# Get url web which contains data for scrape
url = f"https://www.pararius.com/apartments/amsterdam/page-{number}"
page = requests.get(url)
print(page)

# Create object soup
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('section',class_="listing-search-item")

# Makes  CSV file
with open('4.csv','w',encoding='utf8', newline='') as f:
    thewrither = writer(f)
    header = ['Title','Location','Price','Area']
    thewrither.writerow(header)

    for list in lists:
        title = list.find('a',class_="listing-search-item__link--title").text.replace('\n','')
        location = list.find('div',class_="listing-search-item__location").text.replace('\n','')
        price = list.find('span',class_="listing-search-item__price").text.replace('\n','')
        area = list.find('span',class_="illustrated-features__description").text.replace('\n','')
        info = [title,location,price,area]
        thewrither.writerow(info)



