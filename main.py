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
            temp = data[0].get('temp')
            dewp = data[0].get('dewp')
            wspd = data[0].get('wspd')
            wdir = data[0].get('wdir')
            altim = data[0].get('altim')
            return render_template('/metar.html', raw_metar=raw_metar, temp=temp, dewp=dewp, wspd=wspd, wdir=wdir, altim=altim)
        except:
            return render_template('/metar.html', error="Generic error")
        

    elif request.method == 'GET':

        return render_template('/metar.html')
    

@app.route('/airportinfo', methods=['GET', 'POST'])
def airportInfo():

    if request.method == 'POST':
        try:
            airport_icao = request.form.get('icao_input')
            if not airport_icao:
                return render_template('/airportinfo.html', error="Airport code is null")
            response = requests.get(f"https://aviationweather.gov/api/data/stationinfo?ids={airport_icao}&format=json")
            data = response.json()
            if not data:
                return render_template('/airportinfo.html', error="No data returned")
            
            site = data[0].get('site')
            elev = data[0].get('elev')
            lat = data[0].get('lat')
            lon = data[0].get('lon')
            country = data[0].get('country')
            return render_template('/airportinfo.html', site=site, elev=elev, lat=lat, lon=lon, country=country)
        except:
            return render_template('/airportinfo.html', error="Generic error")
        
    elif request.method == 'GET':
        return render_template('/airportinfo.html')    





if __name__ == "__main__":
    app.run(debug=True)
