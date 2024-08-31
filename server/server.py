from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__, static_folder='static')

def create_data(datas):
    data = datetime.now().isoformat()
    num = datas["data"]

    db = sqlite3.connect('servers/bd.db')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT, num TEXT, data TEXT)""")
    db.commit()


    query = f"""INSERT INTO cars (num, data) VALUES('{num}', '{data}')"""
    cursor.execute(query)
    db.commit()
    db.close()
    return view_data()

def view_data():
    db = sqlite3.connect('servers/bd.db')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT, num TEXT, data TEXT)""")
    db.commit()

    view = """SELECT * FROM cars ORDER BY id"""
    cursor.execute(view)
    data = cursor.fetchall()
    db.close()

    if len(data) != 0:
        datas = {}
        for el in data:
        	beforData = datetime.fromisoformat(el[2])
        	nowData = datetime.now()
        	time = str(nowData - beforData)
        	datas.update({ el[0]:{el[1]:time[:time.find(".")]} })
        return datas
    else:
        return {"null":None}

def delate_data(num):
    db = sqlite3.connect('servers/bd.db')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT, num TEXT, data TEXT)""")
    db.commit()

    query = f"""DELETE FROM cars WHERE num = '{num}'"""
    cursor.execute(query)
    db.commit()
    db.close()
    return view_data()


@app.route('/parking/create_data',methods=["POST"])
def create_data_parking():
	data = request.json
	view = create_data(data)

	return jsonify(view)

@app.route('/parking/delete_data',methods=["POST"])
def delate_data_parking():
	data = request.json['del']
	view = delate_data(data)

	return jsonify(view)

@app.route('/parking/view_data',methods=["POST"])
def view_data_parking():
	view = view_data()

	return jsonify(view)