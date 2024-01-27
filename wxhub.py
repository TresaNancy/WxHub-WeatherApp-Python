import requests

city_name = "kochi"
API_Key = '544389e58341d827cc9232f289dc4d74'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key }&units=metric'


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is',data['weather'][0]['description'])
    print('Current temprature is', data['main']['temp'])
    print('current temprature feels like',data['main']['feels_like'])
    print('Humidity is:', data['main']['humidity'])
