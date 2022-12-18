import psycopg2
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
    return valueresult

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