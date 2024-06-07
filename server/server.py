from flask import Flask, request
import sqlite3

def basa_data(datas):
	num, data = datas
	with sqlite3.connect('parking/bd.db') as db:
		cursor = db.cursor()
		querty = """CREATE TABLE IF NOT EXISTS cars(
		num TEXT,
		data TEXT)"""
		cursor.execute(qwerty)
		db.commit()

		qwerty = f"""INSERT INTO cars (num, data) VALUES({num}, {data})"""
		cursor.execute(qwerty)
		db.commit()

app = Flask(__name__)

@app.route('/parking',methods=["POST"])
def index():
	print(request.data.decode())
	basa_data(request.data.decode())
	return "hello world"

if __name__ == '__main__':

    app.run()
