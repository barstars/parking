import requests
from datetime import datetime

# Адрес сервера Flask
url = 'http://127.0.0.17:5050/'

# Данные запроса
data = ['123abc13', datetime.now().isoformat()]

# Отправка POST-запроса с данными
response = requests.post(url, data=data)
print(response.text)
print(type(response.text))
