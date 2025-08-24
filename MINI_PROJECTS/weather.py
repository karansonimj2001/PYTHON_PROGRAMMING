import requests

API_KEY = 'Bd5e378503939ddaee76f12ad7a97608'

city = input("Enter the city name: ")
base_url = "http://api.openweathermap.org/data/2.5/weather"
params = {'q': city, 'appid': API_KEY, 'units': 'metric'}

try:
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print("\nWeather Information:")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print(f"Error: {data['message']}")

except Exception as e:
    print(f"Error: {e}")