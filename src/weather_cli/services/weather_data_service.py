import httpx
from weather_cli.models.current_weather import CurrentWeather

class WeatherDataService():

    @staticmethod
    def get_temparature(latitude, longitude) -> int:
        resp = httpx.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation&current_weather=true')
        
        if resp.is_success:
            current_weather = CurrentWeather.parse_obj(resp.json()["current_weather"])
            return current_weather.temperature
        else:
            raise "Weather API not responsive"

    @staticmethod
    def get_windspeed(latitude, longitude) -> int:
        resp = httpx.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,precipitation&current_weather=true')
        if resp.is_success:
            current_weather = CurrentWeather.parse_obj(resp.json()["current_weather"])
            return current_weather.windspeed
        else:
            raise "Weather API not responsive"