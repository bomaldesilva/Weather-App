import json
from django.shortcuts import render
import urllib


def index(request):
    if request.method == 'POST':
        city=request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=80055909c1cf81684451ae29553c39eb').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(round(json_data['main']['temp']-273.5,2))+'°C',
            "pressure": str(json_data['main']['pressure'])+' Pa',
            "humidity": str(json_data['main']['humidity'])+' g/kg',
        }
    else:
        city=''
        data = {}
    return render(request,'index.html',{'city':city,'data':data})

