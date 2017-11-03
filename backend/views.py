from django.shortcuts import render
from . import views

def home(request):
	return render(request, 'backend/view1.html')

def view2(request):
	return render(request, 'backend/view2.html')