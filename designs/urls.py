from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='designs-index'),
	path('create', views.create, name='designs-create'),
]