from bs4 import BeautifulSoup
from requests import get

"""


"""

class Data:
    """
    Class colletcting data from the website

    Attributes
    ----------
    Fuel : dict[int,string]
        list containing price for the fuel and status (down or up)
    region_data : dict[Name,Fuel]
        list conatining name of the region and Fuel


    """
    General_URL = 'https://www.autocentrum.pl/paliwa/ceny-paliw/'

    page = get(General_URL)
    bs = BeautifulSoup(page.content,features="html.parser")


    for all_regions in bs.find_all('tbody'):            #seperating whole file to get all regions
        for region in all_regions.find_all('tr'):       #seperating get all regions for each region
            name = region.find('a',class_='row-link').get_text()
            print(name)

            all_prices = region.find_all('td', class_='text-center')
            for price in all_prices:
                if (price.find(class_='down')):
                    status = "down"
                elif(price.find(class_='up')):
                    status = "up"
                else:
                    status = ""
                print(price.get_text().strip(),status)  #printing price of petrol and it acutal status







