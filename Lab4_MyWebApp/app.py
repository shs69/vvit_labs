import requests
import psycopg2
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


conn = psycopg2.connect(database='service_db',
                        user='postgres',
                        password='A048kp46',
                        host='localhost',
                        port='5432')

cursor = conn.cursor()


@app.route('/')
def index0():
    return redirect(url_for('login'))


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        cursor.execute("select * from service.users where login=%s and password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        if records:
            return render_template('account.html', full_name=records[0][1], username=username, password=password)
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
