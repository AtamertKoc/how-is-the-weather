# WeatherWise: Dynamic Weather & Clothing Advice

A Python application that integrates with the OpenWeatherMap API to provide real-time weather updates and personalized clothing suggestions.

## Features
- **Real-Time Data:** Fetches live temperature and sky conditions.
- **Smart Logic:** Recommends outfits based on current thermal conditions.
- **Secure Credentials:** Uses environment variables (`.env`) to keep API keys safe.
- **Modular Design:** Clean separation between API services and the main application logic.

## Tech Stack
- **Python 3.14**
- **Requests:** For API communication.
- **Python-dotenv:** For managing environment variables.

## Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AtamertKoc/how-is-the-weather.git
   cd how-is-the-weather
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Configure API Key:**
   ```bash
   Create a .env file in the root directory.
   Add your API key: WEATHER_API_KEY=your_key_here
4. **Run the app:**
   ```bash
   python main.py
