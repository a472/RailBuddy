from django.urls import path
from . import views


urlpatterns =[
	path('', views.home, name='home'),
	path('train_route', views.train_route, name='train_route'),
]