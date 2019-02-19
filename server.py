from flask import Flask, jsonify
from flask import render_template
from flask import request

import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('chat.db')

conn.execute('''CREATE TABLE IF NOT EXISTS messages(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	message TEXT)''')

conn.execute('''CREATE TABLE IF NOT EXISTS user(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT)''')


conn.commit()
conn.close()




@app.route('/')
def home_page():
	return render_template("index.html")


@app.route('/chatapp')
def fetch_all():
	conn = sqlite3.connect('chat.db')
	cur = conn.cursor()

	cur.execute('''SELECT * FROM messages''')

	rows = cur.fetchall()
	return jsonify(rows)

if __name__ == '__main__':
	app.run()