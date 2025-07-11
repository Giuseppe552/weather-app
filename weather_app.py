import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        # wttr.in returns simple JSON weather data
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data = response.json()

        current = data['current_condition'][0]
        temp = current['temp_C']
        desc = current['weatherDesc'][0]['value']
        feels_like = current['FeelsLikeC']

        result = f"{city.title()}: {desc}, {temp}°C (feels like {feels_like}°C)"
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", f"Could not get weather:\n{e}")

# --- GUI ---
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter City Name:").grid(row=0, column=0, padx=10, pady=10)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1)

tk.Button(root, text="Get Weather", command=get_weather).grid(row=1, columnspan=2, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=2, columnspan=2, pady=10)

root.mainloop()
