from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/crud-list/',
        'Create': '/crud-create/',
        'Delete': '/crud-delete/<str:pk>/',
        'Update': '/crud-update/<str:pk>/',
        'Detail View': '/crud-detail/<str:pk>/',
    }
    return Response(api_urls)
