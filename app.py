import psycopg2
import json
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='185.241.192.67',
                            database='pavel',
                            user='postgres',
                            password='postgres')
    return conn

@app.route('/pgetcounthum')
def index():
    param_hum = request.args.get('value')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT getcounthumidity(\'{}\')'.format(param_hum))
    valueresult = cur.fetchall()
    cur.close()
    conn.close()
    return {"hum":valueresult[0][0]}

@app.route('/pgetpass')
def pavelgetpass():
    param_login = request.args.get('login')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT getpass(\'{}\')'.format(param_login))
    passresult = cur.fetchall()
    cur.close()
    conn.close()
    return {"password":passresult[0][0]}

@app.route('/pgetusers')
def pavelgetusers():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from getusertable()')
    passresult = cur.fetchall()
    cur.close()
    conn.close()
    data = [{'Login':item[0],'Password':item[1]} for i, item in enumerate(passresult)]
    return data

@app.route('/pgettemp')
def pavelgettemp():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select gettemperature()')
    passresult = cur.fetchall()
    cur.close()
    conn.close()
    data = [{'value':item[0].replace("(","").replace(")","").split(",")[0],'date':item[0].replace("(","").replace(")","").split(",")[1]} for i, item in enumerate(passresult)]
    return data