#my first DApp
from flask import Flask, render_template, request
import sqlite3
import datetime


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    q = request.form.get('name')
    if q:
        time = datetime.datetime.now().isoformat()
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("INSERT INTO user (name, timestamp) VALUES (?, ?)", (q, time))
        conn.commit()
        conn.close()
    return render_template('main.html')

@app.route('/transferMoney', methods=['GET', 'POST'])
def transferMoney():
    return render_template('transferMoney.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    return render_template('deposit.html')

@app.route('/viewUser', methods=['GET', 'POST'])
def viewUser():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user")
    rows = c.fetchall()
    conn.close()
    return render_template('viewUser.html', rows=rows)

@app.route('/deleteUser', methods=['GET', 'POST'])
def deleteUser():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("DELETE FROM user")
    conn.commit()
    conn.close()
    return render_template('main.html')

if __name__ == '__main__':
    app.run()