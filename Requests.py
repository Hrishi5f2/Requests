import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Error fetching weather data. Please try again later.")
        return None

def get_temperature(date):
    weather_data = get_weather_data()
    if weather_data:
        for entry in weather_data:
            if entry["dt_txt"].startswith(date):
                return entry["main"]["temp"]
        print("Temperature data not found for the given date.")
    return None

def get_wind_speed(date):
    weather_data = get_weather_data()
    if weather_data:
        for entry in weather_data:
            if entry["dt_txt"].startswith(date):
                return entry["wind"]["speed"]
        print("Wind speed data not found for the given date.")
    return None

def get_pressure(date):
    weather_data = get_weather_data()
    if weather_data:
        for entry in weather_data:
            if entry["dt_txt"].startswith(date):
                return entry["main"]["pressure"]
        print("Pressure data not found for the given date.")
    return None

def main():
    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_temperature(date)
            if temperature:
                print(f"Temperature on {date}: {temperature} °C")

        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            if wind_speed:
                print(f"Wind speed on {date}: {wind_speed} m/s")

        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

main()
