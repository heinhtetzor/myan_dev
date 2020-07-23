from django.shortcuts import render, redirect


# Create your views here.
def index(request):
	return render(request, 'designs/index.html')
def create(request):
	return render(request, 'designs/create.html')