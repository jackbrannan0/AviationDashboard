from flask import Flask, render_template, jsonify, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/metar', methods=['GET', 'POST'])
def metar():
    if request.method == 'POST':
        
        try:
            airport_icao = request.form.get('icao_input')
            if not airport_icao:
                return render_template('/metar.html', error="Airport code is null")
            response = requests.get(f"https://aviationweather.gov/api/data/metar?ids={airport_icao}&format=json")
            data = response.json()
            if not data:
                return render_template('/metar.html', error="No data returned")
            raw_metar = data[0]['rawOb']
            return render_template('/metar.html', raw_metar=raw_metar)
        except:
            return render_template('/metar.html', error="Generic error")
        

    elif request.method == 'GET':

        return render_template('/metar.html')
    

@app.route('/airportinfo')
def airportInfo():
    return render_template('/airportinfo.html')



if __name__ == "__main__":
    app.run(debug=True)
