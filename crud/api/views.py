from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def apiOverview(request):
    return JsonResponse("heya this is new api", safe=False)
