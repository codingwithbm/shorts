import requests

# Get the city name from the user
city = input("Enter city name: ")
url = f'http://wttr.in/{city}?format=%C+%t+%w'

# Fetch weather data from wttr.in
response = requests.get(url)
weather = response.text.strip().split()

# Check if the request was successful
if response.status_code == 200 and weather:
    # Extract the weather data
    c, t, w = weather[0], weather[1], weather[2]
    print(f"{city}: {c}, {t}. Wind: {w}")
else:
    print("Error fetching weather data.")
