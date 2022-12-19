import psycopg2
import json
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def get_db_connection():
    conn = psycopg2.connect(host='185.241.192.67',
                            database='pavel',
                            user='postgres',
                            password='postgres')
    return conn

@app.route('/pgetcounthum')
@cross_origin()
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
@cross_origin()
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
@cross_origin()
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
@cross_origin()
def pavelgettemp():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select gettemperature()')
    passresult = cur.fetchall()
    cur.close()
    conn.close()
    data = [{'value':item[0].replace("(","").replace(")","").split(",")[0],'date':item[0].replace("(","").replace(")","").split(",")[1]} for i, item in enumerate(passresult)]
    #return data
    warning = ""
    lastPair = data[len(data)-1]
    print(lastPair)
    #jsonView = json.load(lastPair)
    lastTemperature = lastPair['value']
    print(lastTemperature)

    if((int(lastTemperature)>25) or (int(lastTemperature) < 17)):
        warning = "Осторожно, температура за пределами нормы"

    lastDate = lastPair['date']
    return render_template('index.html',temp=lastTemperature, date =lastDate, warn = warning)


@app.route('/ptemplate')
@cross_origin()
def paveltemplate():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select gettemperature()')
    passresult = cur.fetchall()
    cur.close()
    conn.close()
    data = [{'value': item[0].replace("(", "").replace(")", "").split(",")[0],
             'date': item[0].replace("(", "").replace(")", "").split(",")[1]} for i, item in enumerate(passresult)]
    lastPair = data[len(data) - 1]
    return lastPair

@app.route('/palltempdata')
@cross_origin()
def pavelalltempdata():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select gettemperature()')
    passresult = cur.fetchall()
    cur.close()
    conn.close()
    data = [{'value': item[0].replace("(", "").replace(")", "").split(",")[0],
             'date': item[0].replace("(", "").replace(")", "").split(",")[1]} for i, item in enumerate(passresult)]
    return data
