from django.shortcuts import render
import requests
api_key = 'fp3427nh33'
# api_key = 'fj4ma5chvh'
# Create your views here.

def home(request):
	return render(request, 'base.html')

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
	context={
		'stations':stations,
	}


	return render(request, 'query/train_route.html', context)


def trainBetweenStation(request):
	if request.method=='POST':

		from_st = request.POST.get('from_station')
		dest_st = request.POST.get('to_station')
		date = request.POST.get('date')
		final_url = 'https://api.railwayapi.com/v2/between/source/{}/dest/{}/date/{}/apikey/{}/'.format(from_st, dest_st, date, api_key)
		print(final_url)
		response = requests.get(final_url, params=request.POST)
		data = response.json()

		trains = []
		fields = data['trains']

		for field in fields:
			train = field['number'] + ' - ' + field['name']
			from_st_code = field['from_station']['code']
			src_dep_time = field['src_departure_time']
			to_st_code = field['to_station']['code']
			dest_arr_time = field['dest_arrival_time']

			travel_time = field['travel_time']

			runs_day =[[x['code'],x['runs']] for x in field['days']]  # [[mon,Y],[tue,N].......

			trains.append([train, from_st_code, src_dep_time, to_st_code, dest_arr_time, travel_time, runs_day])

		context = {
			'trains':trains,
			'source':fields[0]['from_station']['name'],
			'dest':fields[0]['to_station']['name'],
		}
		print(final_url)
		return render(request, 'query/trainBetweenStation.html', context)
	return render(request, 'query/trainBetweenStation.html')