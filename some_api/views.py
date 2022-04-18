from django.shortcuts import render
from django.http import JsonResponse  #For creating Json responses

def routeRequest(request):

    responseThing = {"Message": "Hello World"}

    return JsonResponse(responseThing, safe=False)

# Create your views here.
