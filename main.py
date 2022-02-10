
# we will use the Yelp API with Python here

import requests # this is the ULTIMATE Python library for working with APIs
import os
from dotenv import load_dotenv # for my .env file contents

load_dotenv()

API_KEY = os.getenv('API_KEY') # my private Yelp API key

print("--------------------------------- WILDEST YELP REVIEWS ---------------------------------")

business_name = input("Enter a business name: ")
location_name = input("Enter the location you're looking for (city, state, address, or zip code): ")
result_business = {}

business_json = requests.get('https://api.yelp.com/v3/businesses/search', params={'term': business_name, 'location': location_name}, headers={'Authorization': f'Bearer {API_KEY}'}).json() # returns the data for the business that the user entered

businesses = business_json['businesses'] # returns list of dictionaries, each dictionary having a business' info
# print(businesses)
business_ids = [] # each business ID goes here so that we can use the ID to get the business' reviews

for b in businesses: 
    business_ids.append(b['id']) # append each business' ID to the business list
    # print(b['id'])

