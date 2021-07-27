import os
import requests

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()


APIKEY = os.getenv('YA_WEATHER_TOKEN')
CONTENT_TYPE = "application/json"
BASE_URL = "https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}"


@app.get("/", status_code=200)
def read_root():
    return 'OK'


@app.get("/get_weather/", status_code=200)
def get_weather(latitude: float, longitude: float):
    headers = {
        "X-Yandex-API-Key": APIKEY,
    }
    try:
        response = requests.get(
            BASE_URL.format(lat=latitude, lon=longitude),
            headers=headers
        ).json()
    except ValueError as e:
        raise e
    temperature = response.get('fact').get('temp')
    return {'temperature': temperature}
