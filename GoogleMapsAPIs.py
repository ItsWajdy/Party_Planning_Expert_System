import googlemaps
from googleplaces import GooglePlaces, types


class GoogleMaps:
	def __init__(self):
		# self.key = 'AIzaSyBSjAUvigq6Sg07ahdKUXt8P1_GYq9gOWo'
		self.key = 'AIzaSyDnJ6_tO4KJL9qU8cEbq9DXTCX0W3aRgrE'
		self.client = googlemaps.Client(self.key)
		self.location = self.client.geolocate()['location']
		self.radius = 100000

	def get_places_nearby_keyword(self, keyword):
		google_places = GooglePlaces(self.key)

		query_result = google_places.nearby_search(lat_lng=self.location, keyword=keyword, radius=20000,
												   types=[types.TYPE_FOOD])

		if query_result.has_attributions:
			print(query_result.html_attributions)

		for place in query_result.places:
			print(place.name)
			# print(place.geo_location)
			# print(place.place_id)

			place.get_details()
			print(place.local_phone_number)
			print('Website:', place.website)
			print('Open in Google Maps:', place.url)

			# Show photos of place
			# for photo in place.photos:
			# 	# 'maxheight' or 'maxwidth' is required
			# 	photo.get(maxheight=500, maxwidth=500)
			# 	# MIME-type, e.g. 'image/jpeg'
			# 	photo.mimetype
			# 	# Image URL
			# 	photo.url
			# 	# Original filename (optional)
			# 	photo.filename
			# 	# Raw image data
			# 	photo.data

		if query_result.has_next_page_token:
			query_result_next_page = google_places.nearby_search(
				pagetoken=query_result.next_page_token)
