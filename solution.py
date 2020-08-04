# c73c375afbedccd447f98b4e275bb84c
# https://api.darksky.net/forecast/c73c375afbedccd447f98b4e275bb84c/37.8267,-122.4233

import geocoder
import requests
import json

destinations = [
  "The Space Needle",
  "Crater Lake",
  "The Golden Gate Bridge",
  "Yosemite National Park",
  "Las Vegas, Nevada",
  "Grand Canyon National Park",
  "Aspen, Colorado",
  "Mount Rushmore",
  "Yellowstone National Park",
  "Sandpoint, Idaho",
  "Banff National Park",
  "Capilano Suspension Bridge"
]

for i in range(len(destinations)):
  loc = geocoder.arcgis(destinations[i])
  print(f'{destinations[i]} is located at latitude {loc.latlng[0]} longitude {loc.latlng[1]}')