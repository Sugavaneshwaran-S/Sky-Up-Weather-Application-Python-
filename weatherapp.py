import tkinter as tk
import requests
from PIL import Image, ImageTk


app = tk.Tk()

HEIGHT = 400
WIDTH = 800

def format_response(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        country=weather_json['sys']['country']
        temp = weather_json['main']['temp']
        humidity=weather_json['main']['humidity']
        coord1=weather_json['coord']['lon']
        coord2=weather_json['coord']['lat']
        wind=weather_json['wind']['speed']
        wind_deg=weather_json['wind']['deg']
        sr=weather_json['sys']['sunrise']
        ss=weather_json['sys']['sunset']
        final_str = 'City: %s \nConditions: %s \ncountry: %s \nTemperature (°F): %s \nWindspeed (m/s): %s \nDegree (°): %s \nHumidity (per): %s \nLongitude (°): %s \nLatitude (°): %s \nSunrise (UNIX TS): %s \nSunset (UNIX TS): %s' %(city, conditions,country, temp, wind, wind_deg,humidity,coord1,coord2,sr,ss)
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str


def get_weather(city):
    weather_key = '178e6212da56aa7a69f64db5b5f725e8'
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {'APPID': '178e6212da56aa7a69f64db5b5f725e8', 'q': city, 'units':'imperial'}
    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()

    results['text'] = format_response(response.json())

    icon = weather_json['weather'][0]['icon']
    open_image(icon)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./Icons/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img
    

C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
background= tk.PhotoImage(file='./image2.png')
background_label = tk.Label(app, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

f = tk.Frame(app,  bg='#ab09eb', bd=4)
f.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

tb = tk.Entry(f, font=40)
tb.place(relwidth=0.65, relheight=1)

sub = tk.Button(f, text='Get Weather',  bg='#09eb94',font=40, command=lambda: get_weather(tb.get()))
sub.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='#faf9f7', bd=6)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color ='#e00464'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=6)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=5, relheight=5)


app.mainloop()

