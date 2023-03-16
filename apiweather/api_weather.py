import datetime
import requests

class getWeather():

    condition = ''
    temperature = ''
    wind = ''
    city = ''
    time = ''
    def __init__(self, city):
        apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4b84b916703740df2e01f5daf205d9f7"
        json_data = requests.get(apiUrl).json()
        self.condition = str(json_data['weather'][0]['main'])
        self.temperature = str(json_data['main']['temp'] - 273.15)
        self.wind = str(json_data['wind']['speed'])
        self.city = str(city)
        self.time = str(datetime.datetime.now())
    def get_condition(self):
        return self.condition
    def get_city(self):
        return self.city
    def get_wind(self):
        return self.wind
    def get_temperature(self):
        return self.temperature
    def get_time(self):
        return self.time
if __name__ == '__main__':
    api = getWeather('thai nguyen')
    print('wind: ',api.get_wind())
    print('temperature: ',api.get_temperature())
    print('city: ',api.get_city())
    print('condition: ',api.get_condition())
    print('time ', api.get_time())