from django.urls import path
from .import views
urlpatterns = [

    path('',views.home,name="home"),
    path('prices/',views.prices, name="prices"), #THIS IS THE WAY OF SET UL
]
