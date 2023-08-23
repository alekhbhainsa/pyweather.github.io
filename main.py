import requests
import json
import win32com.client as wincl
city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=bbdd067a02a84e1e8a1153624230201&q={city}"
r = requests.get(url)
speak = wincl.Dispatch("SAPI.SpVoice")
# print(r.text)
weitherdic = json.loads(r.text)
temp = weitherdic["current"]["temp_c"]
look = weitherdic["current"]["condition"]["text"]
windsp = weitherdic["current"]["wind_kph"]
visibl = weitherdic["current"]["vis_km"]
humd = weitherdic["current"]["humidity"]
fel = weitherdic["current"]["feelslike_c"]

speak.Speak(f"The current temperature in {city} is {temp} Degree Celsius, its feel like {fel} Degree Celsius , "
            f"humidity is {humd}percent, wind speed is {windsp} kilometer per hour, visibility is {visibl} kilome"
            f"ter it seems{look} sky ")


