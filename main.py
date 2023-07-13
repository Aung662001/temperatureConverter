import customtkinter
import customtkinter as ctk


def validate_entry(text):
    if text.isdigit() or text == "":
        return True
    else:
        return False


def convert_temperature():
    choice = selected_value.get()
    if choice == "C":
        celsius_converter(temperature_entry.get())
    else:
        fahrenheit_converter(temperature_entry.get())


def celsius_converter(x):
    fahrenheit = float(x)
    celsius = (fahrenheit - 32) * 5/9
    celsius_text = f" {celsius:.2f} °C "
    res_text.configure(text=f" {fahrenheit}°F = {celsius_text}", text_color="green", font=ctk.CTkFont(size=20, weight="bold"))


def fahrenheit_converter(x):
    celsius = float(x)
    fahrenheit = (celsius * 9/5)+32
    fahrenheit_text = f" {fahrenheit:.2f} °F"
    res_text.configure(text=f" {celsius}°C = {fahrenheit_text}", text_color="green", font=ctk.CTkFont(size=20, weight="bold"))


window = ctk.CTk()
customtkinter.set_appearance_mode("dark")
window.geometry("600x400")
window.title("Temperature Converter")

title_label = ctk.CTkLabel(window, text="Temperature Converter", font=ctk.CTkFont(size= 30, weight="bold"))
title_label.pack(padx=10, pady=(30, 20))

radio_Frame = ctk.CTkFrame(window)
radio_Frame.pack(fill="x", padx=50)

selected_value = ctk.StringVar(value="C")

radio_FtoC = ctk.CTkRadioButton(radio_Frame, text="Fahrenheit to Celsius", variable=selected_value , value="C")
radio_FtoC.pack(side="left", padx=(80,20), pady=10)

radio_CtoF = ctk.CTkRadioButton(radio_Frame, text="Celsius to Fahrenheit", variable=selected_value, value="F")
radio_CtoF.pack(side="left", padx=(20,10), pady=10)

input_Frame = ctk.CTkFrame(window)
input_Frame.pack(fill="x", padx=50, pady=(30, 20))

temperature_entry = ctk.CTkEntry(input_Frame, placeholder_text="Enter temperature...")
temperature_entry.configure(validatecommand=(temperature_entry.register(validate_entry), "%P"))
temperature_entry.pack(side="left", padx=(80, 10), pady=20)

convert_btn = ctk.CTkButton(input_Frame,text="Convert", command=convert_temperature)
convert_btn.pack(side="left")

display_Frame = ctk.CTkFrame(window)
display_Frame.pack(fill="x", padx=50, pady=(30, 20))

res_text = ctk.CTkLabel(display_Frame, text="")
res_text.pack()
window.mainloop()
