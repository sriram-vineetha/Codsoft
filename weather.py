# Python code for Finding current weather of any city using OpenWeathermap API

# importing requests and json
import requests, json
from bs4 import BeautifulSoup
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = "636c39e1800f5261e407ad7dfd933cd2"
# CITY = "Hyderabad"
CITY= input("Enter city name : ")
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)

# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
    data = response.json()
   # getting the main dict block
    main = data['main']
   # getting temperature
    temperature = main['temp']
   # getting the humidity
    humidity = main['humidity']
   # getting the pressure
    pressure = main['pressure']
   # weather report
    report = data['weather']
    print(f"{CITY:-^40}")
    #Celsius = (Kelvin – 273.15)
    print(f"Temperature (in degree Celcius)): {temperature-273.15}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")
city=input('Enter the city:')
 
# create url
url = "https://www.google.com/search?q="+"weather"+city
 
# requests instance
html = requests.get(url).content
 
# getting raw data
soup = BeautifulSoup(html, 'html.parser')


# get the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
 
# this contains time and sky description
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
 
# format the data
data = str.split('\n')
time = data[0]
sky = data[1]


# list having all div tags having particular clas sname
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
 
# particular list with required data
strd = listdiv[5].text
 
# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]


# printing all the data
print("Temperature is", temp)
print("Day: ", time)
print("Sky Description: ", sky)
print(other_data)
