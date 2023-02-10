# Вывести в текущем и недельном прогнозе скорость ветра и видимость

import requests

city = "Moscow,RU"
appid = "5071b6ba8b9514aa411fe3c5e15a6f3d"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

res_week = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                        params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data2 = res_week.json()

print('Город:', city)
print('Скорость ветра сегодня:', data['wind']['speed'])
print('Видимость сегодня:', data['visibility'])
for i in data2['list']:
    print('Дата:', i['dt_txt'], '\nСкорость ветра:', i['wind']['speed'], '\nВидимость:', i['visibility'])
    print('_________________________')
