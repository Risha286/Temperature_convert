# frontend.py
import tkinter as tk
from tkinter import ttk
import requests

def convert_temperature():
    temperature = float(entry_temperature.get())
    unit = combo_units.get()

    url = 'http://localhost:5000/convert'
    payload = {'temperature': temperature, 'unit': unit}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        lbl_result.config(text=f"Converted Temperatures:\nFahrenheit: {result['fahrenheit']}\nCelsius: {result['celsius']}\nKelvin: {result['kelvin']}")
    else:
        lbl_result.config(text="Error occurred during conversion.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Temperature input field
lbl_temperature = ttk.Label(root, text="Enter temperature:")
lbl_temperature.grid(row=0, column=0, padx=5, pady=5)
entry_temperature = ttk.Entry(root)
entry_temperature.grid(row=0, column=1, padx=5, pady=5)

# Unit selection dropdown
lbl_unit = ttk.Label(root, text="Select unit:")
lbl_unit.grid(row=1, column=0, padx=5, pady=5)
units = ['Celsius', 'Fahrenheit', 'Kelvin']
combo_units = ttk.Combobox(root, values=units)
combo_units.grid(row=1, column=1, padx=5, pady=5)
combo_units.current(0)

# Convert button
btn_convert = ttk.Button(root, text="Convert", command=convert_temperature)
btn_convert.grid(row=2, columnspan=2, padx=5, pady=5)

# Display converted temperature
lbl_result = ttk.Label(root, text="")
lbl_result.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
