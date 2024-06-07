import requests

# Адрес сервера Flask
url = 'http://127.0.0.17:5050/'

# Данные запроса
data = 'python'

# Отправка POST-запроса с данными
response = requests.post(url, data=data)
print(response.text)
print(type(response.text))
