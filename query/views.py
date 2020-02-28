from django.shortcuts import render
import requests

# Create your views here.
def home(request):
	return render(request, 'base.html')

def train_route(request):
	train_number = request.POST.get('train-number')

	api_key = 'fj4ma5chvh'
	final_url = 'https://api.railwayapi.com/v2/route/train/{}/apikey/{}/'.format(train_number, api_key)

	response = requests.get(final_url, params=request.POST)
	data = response.json()

	stations = []
	routes = data['route']
	for route in routes:
		scharr = route['scharr']
		schdep = route['schdep']
		name = route['station']['name']
		code = route['station']['code']
		distance = route['distance']
		day = route['day']

		stations.append([name, code, scharr, schdep, distance, day])
	context={
		'stations':stations,
	}


	return render(request, 'query/train_route.html', context)