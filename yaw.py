'''
Load and return yandex weather
'''

import datetime
import json
import requests

API_KEY = "b69aa9bd-7e86-42ab-9c51-4c493ae3c5e2"
API_URL = "https://api.weather.yandex.ru/v2/informers"
API_HEADERS = {"X-Yandex-API-Key": API_KEY}
API_PARAMS = {"lat": '55.163333',
              "lon": '38.376865',
              "lang": 'ru_RU'
              }


def weather_load() -> None:
    '''
    Load and save to file
    '''
    result = requests.get(url=API_URL,
                          params=API_PARAMS,
                          headers=API_HEADERS).text
    result = json.loads(result)
    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(filename+'.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)


class Weather:
    '''
    Weather data
    '''
    temperature: int = 0
    pressure: int = 760


def weather_get() -> Weather:
    '''
    Return weather
    '''
    result = Weather()
    result.temperature = 20
    result.pressure = 740
    return result


print(weather_get().temperature, weather_get().pressure)
