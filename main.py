import requests
import json

city = input("Enter the city name : ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR-API-KEY=metric"
try:
    p = requests.get(url)
    data = json.loads(p.text)
    temp = data["main"]["temp"]
    humi = data["main"]["humidity"]
    sped = data["wind"]["speed"]
    print(f"The temperature is {temp} °C")
    print(f"The humidity is {humi} %")
    print(f"The speed is {sped} km/h")
except:
    print("Sorry, I couldn't find that city")
