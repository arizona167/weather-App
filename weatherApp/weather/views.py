import requests
import json
from django.shortcuts import render
from .models import City
from .forms import CityForm


def about(request):
	url ="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0b403d8cbc641f739c3c2547ccd9cf75"
	#city = 'Port Harcourt'
	#url = API_Address + city

	
	if request.method == 'POST':
	   form = CityForm(request.POST)
	   if form.is_valid():
	   	form.save()
	else:
		form = CityForm()

	city = City.objects.all()

	#weather_data = []

	  
	r = requests.get(url.format(city)).json()
	

	city_weather_details = {
			   'City': form,
			   'description': r['weather'][0]['description'],
			   'Windspeed':r['wind']['speed'],
			   #'Icon':response['weather'][0]['icon'],
			   # 'Temperature':response['main']['temp'],
        }



	#weather_data.append(city_weather_details)
	context = {'city_weather_details':city_weather_details, 'form' : form}

	return render(request,'weather/weather.html', context)
