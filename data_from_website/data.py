from bs4 import BeautifulSoup
from requests import get

"""


"""

class Data:
    """
    Class colletcting data from the website

    Attributes
    ----------

    Region_data : dict[Region_Name,Fuel]
        list conatining name of the region and Fuel

    Fuel : dict[Fuel_Type_Name,[int,string]]
        list containing price for the fuel and its status (down or up)

    """
    Fuel = dict()
    Region_data = dict()

    General_URL = 'https://www.autocentrum.pl/paliwa/ceny-paliw/'

    page = get(General_URL)
    bs = BeautifulSoup(page.content,features="html.parser")
    Fuel_Type_Names = [ "95", "98", "ON", "ON+", "LPG" ]

    for all_regions in bs.find_all('tbody'):            #seperating whole file to get all regions
        for region in all_regions.find_all('tr'):       #seperating all regions for each region
            name = region.find('a',class_='row-link').get_text()
            # print(name)

            all_prices = region.find_all('td', class_='text-center')
            for index, price in enumerate(all_prices):
                if (price.find(class_='down')):
                    status = "down"
                elif(price.find(class_='up')):
                    status = "up"
                else:
                    status = ""
                # print(price.get_text().strip(),status)  #printing price of petrol and it acutal status
                Fuel[ Fuel_Type_Names[ index ] ] = [ price.get_text().strip(), status]
            Region_data[ name ] = Fuel









