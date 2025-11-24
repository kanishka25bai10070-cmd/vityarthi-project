1. Overview

The program performs three major tasks:

Fetch weather data of a city using an online API

Extract temperature & description from the API response

Recommend clothing based on temperature ranges

The system is built using basic Python and the requests library, making it beginner-friendly and easy to run.

 2. Weather Fetching Process

The function get_weather() sends a request to the OpenWeatherMap API and retrieves the current temperature and weather description for the user-entered city.

How It Works Internally

It constructs the API URL:
https://api.openweathermap.org/data/2.5/weather
Sends a request using:

response = requests.get(base_url, params=params)


Checks if the response is successful (status_code == 200)

Extracts:

Temperature → data['main']['temp']

Description → data['weather'][0]['description']

Returned Output

If valid:

return temp, weather_desc
If invalid (wrong city / wrong API key):
return None, None


 3. Clothing Recommendation Logic
The function suggest_clothing(temp) uses temperature ranges to recommend suitable clothes.
Temperature-Based Conditions
Temperature RangeSuggested Clothing≥ 30°CLight T-shirt, shorts, sunglasses20°C – 30°CT-shirt, jeans or skirt, light jacket10°C – 20°CSweater, jacket, long pants0°C – 10°CCoat, warm clothing, scarf, gloves< 0°CHeavy winter jacket, thermal wear, hat, gloves
This logic is implemented using simple if-elif conditions:
if temp >= 30:
    return "Light T-shirt, shorts, sunglasses"
elif 20 <= temp < 30:
    return "T-shirt, jeans or skirt, light jacket if needed"
...


 4. Main Program Flow
The main() function manages the complete workflow:


Stores the API key


Takes user input for the city


Calls get_weather() to fetch temperature


If data is valid:


Prints the temperature


Prints the weather description


Calls suggest_clothing(temp)


Displays clothing suggestions




If invalid:


Prints an error message (e.g., “City not found”)





 5. Example Execution Flow
Input:
Enter city name: Delhi

API returns:


Temperature → 32°C


Description → clear sky


Output:
Temperature in Delhi: 32°C
Weather: clear sky
Recommended Clothing: Light t-shirt, shorts, sunglasses


 6. Key Features
✔ Real-time weather data
✔ Intelligent clothing suggestions
✔ Beginner-friendly Python code
✔ Works for any global city
✔ Uses free OpenWeatherMap API

🔧 7. Technologies Used


Python 3


Requests Library


OpenWeatherMap REST API



