# views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
	return render(response, "scwebsite\index.html", {})

def subhashitam(response):
	return render(response, "scwebsite\subhashitam.html", {})