import requests

def get_weather(api_key, city, date='current'):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}

    if date != 'current':
        params['dt'] = date

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        return None

if __name__ == "__main__":

    api_key = '8e321e25357dea7d9fc45b8aeb386a7d'

    # Przykład użycia dla pogody
    city_name = input("Podaj nazwę miasta: ")
    weather_data = get_weather(api_key, city_name)

    if weather_data:
        print("Pogoda w {}: {}".format(city_name, weather_data))
    else:
        print("Nie udało się pobrać danych pogodowych.")