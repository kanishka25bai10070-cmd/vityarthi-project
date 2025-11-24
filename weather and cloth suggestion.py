import requests

def get_weather(city_name, api_key):
    base_url="https://api.openweathermap.org/data/2.5/weather"
    params={
        "q":city_name,
        "appid":api_key,
        "units":"metric"
    }
    response=requests.get(base_url,params=params)
    if response.status_code==200:
        data=response.json()
        main=data['main']
        weather_desc=data['weather'][0]['description']
        temp=main['temp']
        return temp,weather_desc
    else:
        return None, None
    
def suggest_clothing(temp):
    if temp>=30:
        return"Light t-shirt, shorts,sunglasses"
    elif 20<= temp<30:
        return "T-shirt,jeans or skirt,light jacket if needed"
    elif 10<=temp<20:
        return "Sweater, jacket,long pants"
    elif 0<=temp<10:
        return "Coat, warm clothing, scarf, gloves"
    else:
        return"Heavy winter jacket,thermal wear, gloves, hat, scarf"
    
def main():
    api_key="30be05b7ba4ac7cccb90b504baa8a4f0"
    city=input("Enter city name:")
    temp, description=get_weather(city,api_key)

    if temp is not None:
        print(f"Current tempertaure in city{city}:{temp}°C")
        print(f"Weather condition:{description}")
        clothing=suggest_clothing(temp)
        print(f"Suggested clothing:{clothing}")

    else:
        print("Could not fetch weather data.Please check the city name or API key.")

if __name__ == "__main__":
    main()
    





    


    