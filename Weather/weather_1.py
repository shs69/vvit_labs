# Вывести в текущем и недельном прогнозе скорость ветра и видимость

import requests

city = "Moscow,RU"
appid = "5071b6ba8b9514aa411fe3c5e15a6f3d"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])

res_week = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                        params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data2 = res_week.json()

print("Прогноз погоды на неделю:")
for i in data2['list']:
    print("Дата<", i['dt_txt'], ">\r\nТемпература<", '{0:+3.0f}'.format(i['main']['temp']), ">\r\nПогодные условия<",
          i['weather'][0]['description'], ">")
    print("___________________________________")
