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

		conn = sqlite3.connect('chat.db')
		c = conn.cursor()
		my_text = request.form['text']
		c.execute("INSERT INTO messages (message) values (?)", (message))
		conn.commit()
		conn.close()
		return render_template('index.html')

def gmessage():
	conn = sqlite3.connect('chat.db')
	c = conn.cursor()
	new_messages = c.execute('SELECT * FROM messages').fetchall()
	conn.close()
	return new_messages


@app.route('/gmessage' , methods=['GET'])
def send():
	gmessage()
	return render_template('index.html')




@app.route('/chatapp')
def fetch_all():
	conn = sqlite3.connect('chat.db')
	cur = conn.cursor()

	cur.execute('''SELECT * FROM messages''')

	rows = cur.fetchall()
	return jsonify(rows)

if __name__ == '__main__':
	app.run()