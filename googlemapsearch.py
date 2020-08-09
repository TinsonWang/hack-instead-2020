import googlemaps
from datetime import datetime
import json

##GOOGLEMAPS PART
API_key = "AIzaSyC5hX_ccGsWexNYHYVreA8qsFtG0Kj9MHM"

gmaps = googlemaps.Client(key = API_key)

#Location generality
user_postal_code = 'N1E 6Y5'

#User search generality
user_lat = gmaps.geocode('168 Cityview Drive North, Ontario, Canada')[0]['geometry']['location']['lat']
user_long = gmaps.geocode('168 Cityview Drive North, Ontario, Canada')[0]['geometry']['location']['lng']
user_latlong = (user_lat,user_long)
user_radius = 3000

gmaps_nearby = gmaps.places_nearby(user_latlong,user_radius,type="grocery_or_supermarket")['results']

if not len(gmaps_nearby):
    print("No results nearby! Try expanding your search radius.")
#else:
    #print(gmaps_nearby)
    #gmaps_json = json.dumps(gmaps_nearby)
    #print(gmaps_json)

store_dict = {}
#store_list = []

for store in gmaps_nearby:
    store_dict[store['name']]= store['vicinity']
    #store_location = store['name'] + " at " + store['vicinity']
    #store_list.append(store_location)

print(store_dict)
