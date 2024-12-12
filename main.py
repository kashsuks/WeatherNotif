import requests
import os
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer

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

def getClothingRecommendation(temperature, location, description):
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    
    prompt = f"I'm in {location} and it's {temperature}°C outside with {description} weather. Recommend what I should wear: "
    
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=50)
    
    outputs = model.generate(
        inputs.input_ids, 
        max_length=200, 
        num_return_sequences=1, 
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response.replace(prompt, '').strip()

def main():
    with open("location.txt", "r") as file:
        city = file.readline().strip()

    weatherInfo = getWeather(city)

    with open("weatherData.txt", "r") as file:
        temperature = file.readline().strip()
        description = file.readline().strip()

    clothingAdvice = getClothingRecommendation(temperature, city, description)

    print(f"It is currently {temperature}°C in {city} with {description}\n\n{clothingAdvice}")

if __name__ == "__main__":
    main()