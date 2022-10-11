# app.py
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/mysql")
def get_mysql():
    mydb = mysql.connector.connect(
        #host="mysql-db-1",
        host="db",
        port="3306",
        user="root",
        password="example",
        database="prueba"
        )
    mydb.set_charset_collation('latin1')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ejemplo1")
    myresult = mycursor.fetchall()
    registro_json = []
    registro = {}
    for result in myresult:
        registro = {'campo1': result[0], 'campo2': result[1], 'campo3': result[2]}
        registro_json.append(registro)
        registro = {}
    
    return jsonify(registro_json)
    #return '{} {}'.jsonpay, myresult

@app.route('/hello', methods = ['GET'])
def hello():
    name = request.args.get('name')
    if name is None:
        text = 'Hello!'
    else:
        text = 'Hello ' + name + '!'
    return jsonify({"message": text})

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415