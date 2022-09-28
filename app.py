from flask import Flask, request, jsonify
import time
import datetime

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

@app.get("/nombre")
def get_nombre():
    ts = time.time()
    # print the current timestamp
    #print(ts)
    date_time = datetime.datetime.fromtimestamp( ts )
    datetime_str = date_time.strftime( "%Y/%m/%d'T'%H:%M:%SZ")  
    #print (date_time)
    #print (datetime_str)
    return datetime_str

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415