import requests

API_KEY = "02da993b262730294c1e497754ac3991"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# In order to request from a server, you need to have a base url
# end point, url we want to hit

# city for weather data

city = input("Enter a city name: ")

# Query parameter
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
# Https request
# Want a get request since we are requesting data
response = requests.get(request_url)

# Status code of 200 means succesful
if response.status_code == 200:
    data = response.json() 
    weather = data['weather'][0]['description']
    # Round to Celsius
    temperature = round(data["main"]["temp"] - 273.15, 2)
    feels_like = round(data["main"]["feels_like"] - 273.15, 2)
    
    print("The temperature for the city:", city)
    print("Weather:", weather)
    print("Temperature:",temperature, "celsius")
    print("Feels like:", feels_like, "celsius")
    # Response taken from the json from the website
else:
    print("An error occured.")
