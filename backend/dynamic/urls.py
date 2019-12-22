from django.conf.urls import url
from django.urls import path
from dynamic.views import create_team

urlpatterns = [
    path('create-team', create_team, name = 'create_team'),
]