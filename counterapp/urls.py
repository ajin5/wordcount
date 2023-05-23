from django.urls import path
from counterapp import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('counter', views.counter, name="counter"),

]