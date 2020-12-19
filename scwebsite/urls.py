# urls.py
from django.urls import path

from . import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index', views.index, name='index'),
    path('subhashitam', views.subhashitam, name='subhashitam'),
    path('learn', views.learn, name='learn'),
    path('team', views.team, name='team'),
    path('target', views.target, name='target'),
    path('AboutUs', views.AboutUs, name='AboutUs'),
    path('events', views.events, name='events'),
    path('intern', views.intern, name='intern'),
    path('research', views.research, name='research'),
    path('shaastra', views.shaastra, name='shaastra')
]