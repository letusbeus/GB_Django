from django.urls import path
from lec_05 import views

urlpatterns = [
    path('', views.index, name="index"),
]
