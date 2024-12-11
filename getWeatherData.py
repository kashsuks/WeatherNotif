import requests
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

def getWeather(city):

  load_dotenv(Path(".env"))
  API_KEY = os.getenv("WEATHERAPI")
  baseURL = "http://api.openweathermap.org/data/2.5/weather?"
  completeURL = baseURL + "appid=" + API_KEY + "&q=" + city
  response = requests.get(completeURL)
  if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = round(main['feels_like'] - 273.15, 2)  # Convert from Kelvin to Celsius
    description = data['weather'][0]['description']
    with open("weatherData.txt", "w") as file:
      file.write (f"{temperature}\n{description}\n")
    return f"{temperature},{description}"
  else:
    return "City not found or an error occurred."



if __name__ == "__main__":
  city = input("Enter city name: ")
  weatherInfo = getWeather(city)
  print(weatherInfo)