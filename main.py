from flask import Flask, render_template, jsonify
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/metar')
def metar():
    return render_template('/metar.html')

@app.route('/airportinfo')
def airportInfo():
    return render_template('/airportinfo.html')

@app.route('/metar')
def getMetar():
    try:
        response = requests.get("https://aviationweather.gov/api/data/metar?ids=EGSS&format=json")
        data = response.json()
        raw_metar = data[0]['rawOb']
        return render_template(raw_metar=raw_metar)
    except:
        return ("Data Invalid", 400)  


if __name__ == "__main__":
    app.run(debug=True)
