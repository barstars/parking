from flask import Flask, request, jsonify
import sqlite3

def create_data(datas):
	num = list(datas.keys())[0]
	data = datas[num]
	db = sqlite3.connect('parking/bd.db')
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS cars(num TEXT,data TEXT)""")
	db.commit()

	if len(view_data(num=num)) == 0:
		qwerty = f"""INSERT INTO cars (num, data) VALUES('{num}', '{data}')"""
		cursor.execute(qwerty)
		db.commit()
		db.close()
		return "Success"
	else:
		return "Такое уже есть"

def view_data(num = '0'):
	db = sqlite3.connect('parking/bd.db')
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS cars(num TEXT,data TEXT)""")
	db.commit()
	if num != '0':
		view = f"""SELECT * FROM cars WHERE num = '{num}'"""
		cursor.execute(view)

		data = cursor.fetchall()
		db.close()
		return data
	else:
		view = f"""SELECT * FROM cars"""
		cursor.execute(view)
		data = cursor.fetchall()
		db.close()
	if len(data) != 0:
		datas = {}
		for el in data:
			datas.update({el[0]:el[1]})

		return datas
	else:
		return {None:None}

def delate_data(num):
	db = sqlite3.connect('parking/bd.db')
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS cars(num TEXT,data TEXT)""")
	db.commit()

	qwerty = f"""DELETE FROM cars WHERE num = '{num}'"""
	cursor.execute(qwerty)
	db.commit()
	db.close()
	return "Success"


app = Flask(__name__)

@app.route('/parking/create_data',methods=["POST"])
def create_data_parking():
	data = request.json
	status = create_data(data)
	
	return status

@app.route('/parking/delate_data',methods=["POST"])
def delate_data_parking():
	data = request.data.decode()
	status = delate_data(data)
	
	return status

@app.route('/parking/view_data',methods=["POST"])
def view_data_parking():
	view = view_data()
	
	return jsonify(view)

if __name__ == '__main__':

    app.run()
