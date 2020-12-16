# views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
	return render(response, "scwebsite\index.html", {})

def subhashitam(response):
	return render(response, "scwebsite\subhashitam.html", {})

def team(response):
	return render(response, "scwebsite\team.html", {})


def target(response):
	return render(response, "scwebsite\target.html", {})


def learn(response):
	return render(response, "scwebsite\learn.html", {})
	