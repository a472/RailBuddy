from django.shortcuts import render
import requests

api_key = '3v49bc4x7p'


# Create your views here.

def home(request):
	return render(request, 'base.html')


def liveTrainStatus(request):
	return render(request, 'query/liveTrainStatus.html')


def fare_enquiry(request):
	if request.method=='POST':
		train_number = request.POST.get('train_number')
		source_stn_code = request.POST.get('source_stn_code')
		dest_stn_code = request.POST.get('dest_stn_code')
		age = request.POST.get('age')
		prefs = request.POST.get('class_code')
		quota = request.POST.get('quota_code')
		dated = str(request.POST.get('date'))
		print(dated)
		dd = str(dated[8:])
		mm = str(dated[5:7])
		yyyy = str(dated[:4])
		date = dd + '-' + mm + '-' + yyyy

		final_url = 'https://api.railwayapi.com/v2/fare/train/{}/source/{}/dest/{}/age/{}/pref/{}/quota/{}/date/{}/apikey/{}/'.format(
			train_number, source_stn_code, dest_stn_code, age, prefs, quota, date, api_key)
		print(final_url)
		response = requests.get(final_url, params=request.POST)
		data = response.json()
		fare = data['fare']
		return render(request, 'query/fare_enquiry.html', {'fare': fare})
	return render(request, 'query/fare_enquiry.html')


def train_route(request):
	train_number = request.POST.get('train-number')
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
	context = {
		'stations': stations,
	}
	return render(request, 'query/train_route.html', context)