from flask import Flask, render_template
from subprocess import check_output
import json
import dataset
import threading

app = Flask(__name__)
app.config['DEBUG'] = True

db = dataset.connect('sqlite:///database.db')
table = db['temperaturevalues']

@app.route("/")
def hello():
    return render_template('temperatures.html')

@app.route("/currenttemperature")
def temperature():
    return check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"])

@app.route("/temperatures")
def temperatures():
    data = []
    for value in table.find(_limit=30, order_by='-id'):
        data.append(value)
    return json.dumps(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
