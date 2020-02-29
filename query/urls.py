from django.urls import path
from . import views


urlpatterns =[
	path('', views.home, name='home'),
	path('fare-enquiry', views.fare_enquiry, name='fare_enquiry'),
	path('live-train-status', views.liveTrainStatus, name='liveTrainStatus'),
	path('train_route', views.train_route, name='train_route'),
]