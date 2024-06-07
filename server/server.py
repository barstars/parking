from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/',methods=["POST"])
def index():
	print(request.data.decode())
	return "hello world"

if __name__ == '__main__':
    app.run()
