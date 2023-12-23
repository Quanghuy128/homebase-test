from bs4 import BeautifulSoup
from realestate import RealEstate
import requests
import pandas as pd 

cache = dict() # cache dictionary #Url - Response#

website = "https://sosanhnha.com/"

def fetch(url:str): 
    headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'})
    return requests.get(website, headers=headers)

def get_cached_response(url):
    if url not in cache:    
        cache[url] = fetch(url)
    return cache[url]

response = get_cached_response(website)

soup = BeautifulSoup(response.content, "html.parser")

results = soup.find_all("div", {"class" : "item"})

real_estates = []
for result in results:
    title = result.find('a', {'class':'title'}).get_text() if result.find('a', {'class':'title'}) is not None else "No Data"
    price = result.find('strong', {'class':'price'}).get_text() if result.find('strong', {'class':'price'}) is not None else "No Data"
    area = result.find('strong', {'class':'acreage'}).get_text() if result.find('strong', {'class':'acreage'}) is not None else "No Data"
    address = result.find('strong', {'class':'address'}).get_text() if result.find('strong', {'class':'address'}) is not None else "No Data"
    owner = result.find('span', {'class':'phone_name'}).get_text() if result.find('span', {'class':'phone_name'}) is not None else "No Data"
    contact_number = result.find('span', {'class':'phone_number'}).get_text() if result.find('span', {'class':'phone_number'}) is not None else "No Data"
    
    real_estate = RealEstate(title, price, area, address, owner, contact_number)
    real_estates.append(real_estate)
    
[print(res) for res in real_estates]

df = pd.DataFrame([x.as_dict() for x in real_estates])
df.to_csv('realestate.csv', index=False)

