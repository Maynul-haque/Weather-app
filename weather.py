from tkinter import *
from turtle import width
from customtkinter import *

import requests

def weather():
    # city_name = city_listbox.get()
    city_name = city_name_search.get()
    city_name_search.delete(0,"end")
    API_key = "85121e78f077658c649e40edca439692"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
    res = requests.get(url)
    output = res.json()

    try:
        name_city = output['name']
        weather_status= output['weather'][0]['description']
        temperature = output['main']["temp"]
        humidity = output['main']["humidity"]
        wind_speed = output['wind']['speed']

        name_city_label.config(text = f"Name of city : {name_city}")
        weather_status_label.config(text = f"Weather Status : {weather_status}")
        temperature_label.config(text = f"Temperature : {temperature} ")
        humidity_label.config(text = f"Humidity : {humidity}")
        wind_speed_label.config(text = f"Wind Speed : {wind_speed}")

    except KeyError:
        name_city_label.config(text = "")
        weather_status_label.config(text = "")
        temperature_label.config(text = "City not found")
        humidity_label.config(text = "")
        wind_speed_label.config(text = "")

    
    
def temp_text(e):
   city_name_search.delete(0,"end")




window =CTk()
window.geometry("400x300")
window.title("Current Weather")
set_appearance_mode("System")

# city_name_list = ["Dhaka","Comilla", "Chittagong"]


def temp_text(e):
   city_name_search.delete(0,"end")
city_name_search = Entry(window, text = "enter name of city",  width= 50)
city_name_search.insert(0, "Enter name Of the city.... ")
city_name_search.grid(row =0, column = 2, pady= 10)
city_name_search.bind("<FocusIn>", temp_text)

# city_listbox = StringVar(window)
# city_listbox.set("Select the city")

# option = OptionMenu(window, city_listbox, *city_name_list)
# option.grid(row = 2, column= 2,padx= 150, pady= 10)

b1 = CTkButton(master=window, text = "Search" , corner_radius=10, command= weather)
b1.grid(row = 7, column= 2,padx= 150)

name_city_label = Label(window, font = ("railway", 10, "bold"))
name_city_label.grid(row= 8, column = 2)

weather_status_label = Label(window, font = ("railway", 10, "bold"))
weather_status_label.grid(row= 10, column = 2)

temperature_label = Label(window, font = ("railway", 10, "bold"))
temperature_label.grid(row= 12, column = 2)

temperature_label = Label(window, font = ("railway", 10, "bold"))
temperature_label.grid(row= 12, column = 2)

humidity_label = Label(window, font = ("railway", 10, "bold"))
humidity_label.grid(row= 14, column = 2)

wind_speed_label = Label(window, font = ("railway", 10, "bold"))
wind_speed_label.grid(row= 16, column = 2)



window.mainloop()