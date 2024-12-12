import requests
import os
from dotenv import load_dotenv
from transformers import pipeline

def getWeather(city):
    load_dotenv()
    apiKey = os.getenv('WEATHERAPI')
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    completeUrl = baseUrl + "appid=" + apiKey + "&q=" + city
    response = requests.get(completeUrl)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = round(main['feels_like'] - 273.15, 2)
        description = data['weather'][0]['description']
        with open("weatherData.txt", "w") as file:
            file.write(f"{temperature}\n{description}\n")
        return f"{temperature},{description}"
    else:
        return "City not found or an error occurred."

def getClothingRecommendation(temperature, location):
    qaPipeline = pipeline(
        "conversational", 
        model="facebook/blenderbot-400M-distill"
    )

    prompt = f"I'm in {location} and it's {temperature}°C outside with {description}. What should I wear to be comfortable and appropriate for the weather? Give me specific clothing recommendations."

    response = qaPipeline(prompt)[0]['generated_text']
    
    return response

def main():
    with open("location.txt", "r") as file:
        city = file.readline().strip()

    weatherInfo = getWeather(city)

    with open("weatherData.txt", "r") as file:
        temperature = file.readline().strip()
        description = file.readline().strip()

    clothingAdvice = getClothingRecommendation(temperature, city)

    print(f"It is currently {temperature}°C in {city} with {description}\n\n{clothingAdvice}")

if __name__ == "__main__":
    main()