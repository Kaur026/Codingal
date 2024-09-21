from Flask import Flask, render_template, request
import json
import urllib.request

app= flask(__name__)
@app.route('/getWeather', methods=['POST','GET'])

def weather():
    if request.method=='POST':
        location = request.form['city']

    else:
        location='chennai'
        api="e0b19566bba38f97d53743b5e55c8662"

    try:
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='+
            location+ '&appid=' + api).read()
             
        responseData = json.loads(source)

        data = {
                 "country_code":str(responseData['sys']['country']),
                 "temp":str(responseData['amu']['temp'])+'k',
                 "locatuion": str(responseData['name'])
             }
        return render_template('index.html', data=data)

    except (Exception):
           return render_template('indx.html',error="Give the correct location")
@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080)
    
