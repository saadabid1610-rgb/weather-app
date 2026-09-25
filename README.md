# Weather App 🌤️

A simple Python weather application that fetches real-time weather information using the WeatherAPI.

## Features

* Search weather by city name
* Shows current temperature in Celsius
* Shows current weather condition
* Uses WeatherAPI
* API key is stored securely using environment variables

## Technologies Used

* Python
* Requests
* python-dotenv
* WeatherAPI

## Setup

1. Clone this repository.
2. Install the required packages:

```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project folder:

```env
WEATHER_API_KEY=your_api_key_here
```

4. Run the application:

```bash
python Weather.py
```

## Security

The API key is stored in `.env` and is excluded from Git using `.gitignore`.

## Author

Saad
