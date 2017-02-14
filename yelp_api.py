# import requests
# from constant import app_id, app_secret

# data = {'grant_type': 'client_credentials',
#         'client_id': app_id,
#         'client_secret': app_secret}
# token = requests.post('https://api.yelp.com/oauth2/token', data=data)
# access_token = token.json()['access_token']
# url = 'https://api.yelp.com/v3/businesses/search'
# headers = {'Authorization': 'bearer %s' % access_token}
# params = {
#           'term': 'Restaurant',
#           'sort_by': 'review_count',
#           'bounds': '37.900000,-122.500000|37.788022,-122.399797',
#           'limit': 5
#          }

# resp = requests.get(url=url, params=params, headers=headers)
# print resp.json()
import time
from yelp.api.v2 import Yelp
from constant import consumer_key,consumer_secret,token,token_secret
import pandas as pd 
def rectangle(l1,l2,l3,l4):
    time1 = time.time()

    yelp = Yelp(
        consumer_key,
        consumer_secret,
        token,
        token_secret,
    )
    # print "prepare data"
    # print str(l1) + ','+ str(l2) +'|'+ str(l3) +','+ str(l4)
    restaurants = yelp.search(term='food',bounds=str(str(l1) + ','+ str(l2) +'|'+ str(l3) +','+ str(l4)))
    # restaurants.get('businesses')
    time2 = time.time()
    print '%s function took %0.3f ms' % ("rip", (time2-time1)*1000.0)
    


    category = []
    location = []
    longitude = []
    latitude = []
    rating = []
    review_count = []
    url = []
    image = []
    name = []
    for i in restaurants.get('businesses'):
        category.append(i.get("categories")[0][0] )
        location.append(i.get("location").get('address')[0] + " " + i.get("location").get('city') + " " + i.get("location").get('state_code') + " " + i.get("location").get('postal_code'))
        longitude.append(i.get('location').get('coordinate').get('longitude'))
        latitude.append(i.get('location').get('coordinate').get('latitude'))
        rating.append(i.get('rating'))
        review_count.append(i.get('review_count'))
        url.append(i.get('url'))
        image.append(i.get('image_url'))
        name.append(i.get('name'))

    rest_info = pd.DataFrame({"name": name, "category": category, "address": location, "latitude": latitude, "longitude": longitude,
                  "stars": rating, "review_count": review_count, "url": url, "image": image})


    return rest_info

# rectangle(37.900000,-122.500000,37.788022,-122.399797)





