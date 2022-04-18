from django.urls import path
from . import views


urlpatterns = [
    path('', views.routeRequest, name='routes'),
]