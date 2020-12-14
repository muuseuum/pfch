import requests
import json
import time

#put your API key
key = 'API INFO'

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

all_data = {
}


#put the lat/long information 
search_lat_long = ['40.7575544685112, -73.9864720166591', '40.739711859825746, -73.99105045360372']
for coords in search_lat_long:

	params = {
		'key' : key,
		'location' : coords,
		'fields' : 'name,business_status,permanently_closed,formatted_address,geometry,types,place_id',
		'radius' : '1000',
		'type' : 'restaurant',
	}

	r = requests.get(url, params=params)
	data = json.loads(r.text)
	
	for restaurant in data['results']:
		all_data[restaurant['place_id']] = restaurant

#1 sec was not enough to get data so I set 5secs in the time.sleep() section 
	while 'next_page_token' in data:
		time.sleep(5)
		print('--------')
		new_params = {
			'key' : key,
			'pagetoken': data['next_page_token']
		}

		r = requests.get(url, params=new_params)		
		data = json.loads(r.text)

		for restaurant in data['results']:
			all_data[restaurant['place_id']] = restaurant
	


json.dump(all_data,open('places.json','w'),indent=2)

