from flask import Flask, jsonify
from flask import render_template
from flask import request

import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('chat.db')

conn.execute('''CREATE TABLE IF NOT EXISTS messages(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	message TEXT,
	id_sender INTEGER,
	id_receiver INTEGER, 
	FOREIGN KEY(id_sender) REFERENCES users(id), 
	FOREIGN KEY(id_receiver) REFERENCES users(id))''')

conn.execute('''CREATE TABLE IF NOT EXISTS user(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT)''')


conn.commit()
conn.close()




@app.route('/' , methods=['POST'])
def home_page():

	name = request.form['name']
	message = request.form['message']

	if name and message:
		newName = name[::-1]

		return jsonify({'name' : newName})

	return jsonify({'error' : 'Missing data!'})
	return render_template("index.html")


@app.route('/smessage')
def send():
	sender = request.form.get('sender')	
	amessage = request.form.get('message')
	receiver = request.form.get('receiver')

	print(sender)
	print(receiver)

	connection = sqlite3.connect('chat.db')
	c = connection.cursor()





@app.route('/chatapp')
def fetch_all():
	conn = sqlite3.connect('chat.db')
	cur = conn.cursor()

	cur.execute('''SELECT * FROM messages''')

	rows = cur.fetchall()
	return jsonify(rows)

if __name__ == '__main__':
	app.run()