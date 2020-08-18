from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('newtrip', views.new_trip_form),
    path('trip/new', views.new_trip)
    path('trip_info/<int:id>', views.trip_info')
]