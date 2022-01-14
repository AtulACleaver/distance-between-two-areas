from geopy.distance import geodesic
import requests
import urllib.parse

location_1 = input("Name of first location: ")
location_2 = input("Name of second location: ")

url_1 = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location_1) + '?format=json'
url_2 = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location_2) + '?format=json'

response_1 = requests.get(url_1).json()
response_2 = requests.get(url_2).json()

lat_location_1 = response_1[0]["lat"]
lon_location_1 = response_1[0]["lon"]

lat_location_2 = response_2[0]["lat"]
lon_location_2 = response_2[0]["lon"]

co_1 = (lat_location_1, lon_location_1)
co_2 = (lat_location_2, lon_location_2)

# Print the distance calculated in km
print(f'')
print(f"The distance between {location_1} and {location_2} is: {round(geodesic(co_1, co_2).km, 2)} km")
