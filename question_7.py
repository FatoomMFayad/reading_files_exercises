#Write a Python program to read the JSON data from the link: https://gbfs.citibikenyc.com/gbfs/en/station_information.json , retrieve only the capacities of all stations and store them in a list.
import requests
import json

url = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
data = requests.get(url).json()
capacities = [station['capacity'] for station in data['data']['stations']]

print(capacities)