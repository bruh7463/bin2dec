from django.urls import path

from . import views

app_name = 'bin2dec_app'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
]