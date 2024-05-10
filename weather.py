import requests

my_api_key = "a65a485be3aeabf94bda30cbb253d554"

user_input = input("Enter the city for weather report: ")
print(user_input);

data_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={my_api_key}")

if data_weather.json()['cod'] == '404':
    print("City not found.")
else:
    city_weather = data_weather.json()['weather'][0]['main']
    city_temperature = round(data_weather.json()['main']['temp'])
    max_temperature = round(data_weather.json()['main']['temp_max'])
    min_temperature = round(data_weather.json()['main']['temp_min'])
    city_humidity = round(data_weather.json()['main']['humidity'])
    city_windspeed = round(data_weather.json()['wind']['speed'])
    city_pressure = round(data_weather.json()['main']['pressure'])

print(f"The weather in {user_input} is: {city_weather}")
print(f"The temperature in {user_input} is: {city_temperature} F")
print(f"The maximum temperature in {user_input} is: {max_temperature} C")
print(f"The minimum temperature in {user_input} is: {min_temperature} C")
print(f"The humidity in {user_input} is: {city_humidity} %")
print(f"The wind speed in {user_input} is: {city_windspeed} km/hr")
print(f"The pressure in {user_input} is: {city_windspeed} Pa")
