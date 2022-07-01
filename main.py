from bs4 import BeautifulSoup
from requests import get

General_URL = 'https://www.autocentrum.pl/paliwa/ceny-paliw/'

page = get(General_URL)
bs = BeautifulSoup(page.content,features="html.parser")


for all_regions in bs.find_all('tbody'):
    for region in all_regions.find_all('tr'):
        name = region.find('a',class_='row-link').get_text()
        print(name)
        #print(region)
        all_prices = region.find_all('td', class_='text-center')
        for price in all_prices:
            if (price.find(class_='down')):
                status = "down"
            elif(price.find(class_='up')):
                status = "up"
            else:
                status = ""
            print(price.get_text().strip(),status)
        #print(all_prices)






