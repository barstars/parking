import requests
from datetime import datetime

def data_view():
	url = 'http://127.0.0.1:5000/parking/view_data'

	# Данные запроса
	data = {'1':'1'}

	# Отправка POST-запроса с данными
	response = requests.post(url, json=data)
	dic = response.json()
	data_keys = list(dic.keys())
	res = []
	for el_key in data_keys:
		res.append([el_key, dic[el_key], str(datetime.now()-datetime.fromisoformat(dic[el_key]))])
	return res

def data_create(data):
	url = 'http://127.0.0.1:5000/parking/create_data'

	# Данные запроса
	time = datetime.now().isoformat()
	data = {data:time}

	# Отправка POST-запроса с данными
	response = requests.post(url, json=data)
	return response.text

def data_delate(data):
	url = 'http://127.0.0.1:5000/parking/delate_data'
	response = requests.post(url, data=data)
	return response.text


print(data_create('123abc13'))
print(data_view())
print(data_delate('123abc13'))
print(data_view())