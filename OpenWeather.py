import requests
import pandas as pd
import openpyxl
import json
import logging
from dotenv import load_dotenv
import os

path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(path):
    load_dotenv(path)
appid = os.getenv("KEY_API")

def find_city (s_city):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        return data['list'][0]['id']
    except Exception as e:
        logging.error(f"Такого города нет в справочнике {s_city}! {e}")
        pass

def get_weather_data (city_id):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        df = pd.DataFrame({'temp now': data['main']['temp'],
                           'temp_min': data['main']['temp_min'],
                            'temp_max':data['main']['temp_max'],
                            'pressure': data['main']['pressure'],
                            'humidity':data['main']['humidity'],
                            'wind speed': data['wind']['speed'],
                            'city': data['name']},
                            index=[0])
        return df

    except Exception as e:
        logging.error(f"Ошибка при получении погоды для города {city_id}! {e}")
        pass

logging.basicConfig(filename="sample.log", level=logging.INFO)
datafr = pd.DataFrame()
try:
    f = open('city.json', 'r')
except Exception as e:
    logging.error("Не найден файл!", e)
str = f.read()
items = json.loads(str)

for key in items:
    logging.info(f"Попытка найти город {items[key]} в справочнике")
    city_id = find_city(items[key])
    if city_id is not None:
        logging.info(f"Получение информации по городу {items[key]}")
        datafr = pd.concat([datafr, get_weather_data (city_id)], ignore_index=True)

if datafr is not None:
    logging.info(f"Запись информации о погоде в Excel")
    datafr.to_excel("weather.xlsx")