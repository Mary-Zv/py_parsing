#2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
# Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию.
# Ответ сервера записать в файл.

#Если нет желания заморачиваться с поиском, возьмите API вконтакте (https://vk.com/dev/first_guide).
# Сделайте запрос, чтобы получить список всех сообществ на которые вы подписан


import requests
import json
from pprint import pprint

end_point = 'https://api.vindecoder.eu/3.1'
api_key = '53868031779e'
secret_key = '4c89f10f80'
id = 'decode'
vin = input('Введите VIN код автомобиля - ')

url = f'{end_point}/{api_key}/{secret_key}/{id}/{vin}.json'

req = requests.get(url)
data = json.loads(req.text)
print(data)

with open("data_file.json", "w") as file:
    json.dump(data, file)