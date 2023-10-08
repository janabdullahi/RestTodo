from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CrudSerializers
from .models import Crud

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

@api_view(['GET'])
def crudList(request):
    crud = Crud.objects.all()
    serializer = CrudSerializers(crud, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def crudDetail(request,pk):
    crud = Crud.objects.get(id=pk)
    serializer = CrudSerializers(crud, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def crudCreate(request):
    serializer = CrudSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def crudUpdate(request,pk):
    crud = Crud.objects.get(id=pk)
    serializer = CrudSerializers(instance=crud,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def crudDelete(request,pk):
    crud = Crud.objects.get(id=pk)
    crud.delete()
    return Response("The record is deleted successfuly.")