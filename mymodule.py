
from urllib.request import urlopen
import json

def get_weather(city):
    sock = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" +
    city + "&appid=ae4b519fede1df215cc5d3ed8758c521")
    result = sock.read()
    sock.close()
    weather = json.loads(result)
    return weather["main"]["temp"] -273.15

def postal_lookup(postal_code):
    sock = urlopen("http://api.postcodes.io/postcodes/" + postal_code)
    result = sock.read()
    sock.close()
    details = json.loads(result)
    return (details["result"]["latitude"], details["result"]["longitude"])

if __name__ == "__main__":
    degrees = get_weather("OSLO")
    print("weather in Oslo is %.2f" % degrees)
    
    location = postal_lookup("B323PP")
    print(location)
