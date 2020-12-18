# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .shloka import s
# Create your views here.



def index(response):
	return render(response, "scwebsite/index.html", {})

def subhashitam(response):
	return render(response, "scwebsite/subhashitam.html", {})

def team(response):
	team = {'present':
	{('https://dl.dropbox.com/s/mb3etx96fozzyyf/anil%20sir_faculty%20adviser.jpg?dl=0','Prof. Anil Gourishetty','Faculty Advisor'),
	('https://dl.dropbox.com/s/ekzp7ysbiphwp3t/Abhilash_.jpg?dl=0','Abhilash','Executive Member'),
	('https://dl.dropbox.com/s/07y3u9qz1inu54b/Nikunj.jpg?dl=0','Nikunj','Executive Member'),
	('https://dl.dropbox.com/s/qpoxroyic7tty6u/Pratigya.jpg?dl=0','Raghudev','Executive Member'),
	('https://dl.dropbox.com/s/s3shee0rjjyxl4e/Prasiddha.jpg?dl=0','Prasiddha','Executive Member'),
	('https://dl.dropbox.com/s/2e0r5v9remxfl1s/Bhaskar.jpg?dl=0','Bhaskar','Executive Member'),
	('https://dl.dropbox.com/s/8xfi8962ssblu3k/Anjali.jpg?dl=0','Anjali','Executive Member'),
	('https://dl.dropbox.com/s/6x0b5aihfm56cfg/Mohak.jpeg?dl=0','Mohak','Executive Member'),
	('https://dl.dropbox.com/s/788e01an7btcu43/Radheesh.jpeg?dl=0','Radheesh','Executive Member'),
	('https://dl.dropbox.com/s/8uabacj8185yo8v/Janhavi.jpeg?dl=0','Janhavi','Executive Member'),
	('https://dl.dropbox.com/s/i5racp48xkiv5ms/Shubham.jpg?dl=0','Shubham','Executive Member'),
	('https://dl.dropbox.com/s/xxozj1ptb9bd5yp/Vishal.jpg?dl=0','Vishal','Executive Member')
	},
	'alumni':
	{('https://dl.dropbox.com/s/at12cf9itw2dn0a/Sonali_face.jpg?dl=0','Sonali','Alumnus'),
	('https://dl.dropbox.com/s/ojvjuy1otthojgw/Ravi.jpg?dl=0','Ravi','Alumnus'),
	('https://dl.dropbox.com/s/kpamsqkeqwmf7qs/Gargi_face.jpg?dl=0','Gargi','Alumnus'),
	('https://dl.dropbox.com/s/sws83fm8qhnzoee/Mrigank_face.jpg?dl=0','Mrigank','Alumnus'),
	('https://dl.dropbox.com/s/3uu2vwiwkrz0ku6/Anula_face.jpg?dl=0','Anula','Alumnus'),
	('https://dl.dropbox.com/s/167497vl6f9x4ik/Eklavya_face.jpg?dl=0','Eklavya','Alumnus'),
	('https://dl.dropbox.com/s/uo0wlwctj81dqnm/Mihir.jpg?dl=0','Mihir','Alumnus'),
	('https://dl.dropbox.com/s/kkkx166fd0b62pu/Yagya.jpg?dl=0','Yagya','Alumnus')
	}}
	return render(response, "scwebsite/team.html", team)

def target(response):
	return render(response, "scwebsite/target.html", {})

def learn(response):
	return render(response, "scwebsite/learn.html", s)
	