import tkinter as tk
import requests

API_KEY = 'f32d7343dcd0e00841eefa7234a5f9c9'

def fetch_weather(city_name):
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()
        weather_description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        result_label.config(text=f"Condition: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%")
    except Exception as e:
        result_label.config(text="Error fetching data")

def get_weather():
    city = city_entry.get()
    fetch_weather(city)


app = tk.Tk()
app.title("Weather Forecast App")

# Create widgets
title_label = tk.Label(app, text="Weather Forecast", font=("Helvetica", 22))
city_label = tk.Label(app, text="Enter City:",font=("times new roman",16))
city_entry = tk.Entry(app)
search_button = tk.Button(app, text="Search",font=("times new roman",16), command=get_weather)
result_label = tk.Label(app, text="", justify="left")

# Place widgets on the window
title_label.pack(pady=30)
city_label.pack()
city_entry.pack()
search_button.pack(pady=30)
result_label.pack()

# Start the Tkinter main loop
app.mainloop()
