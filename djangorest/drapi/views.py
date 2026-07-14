from django.shortcuts import render
from .models import Aiquest
from.serializers import AiquestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def aiquest_create(request, pk=None):
    if request.method == 'GET':
        id = pk
        #Spacific data show
        if id is not None:
            #compelx data
            ai = Aiquest.objects.get(id=id)
            #python dictionary
            serializer = AiquestSerializer(ai)
            return Response(serializer.data)
        #all data show
        #complex data
        ai = Aiquest.objects.all()
        #python dictionary
        Serializer = AiquestSerializer(ai, many=True)
        return Response(Serializer.data)




"""from django.shortcuts import render
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.
#Queryset
def aiquest_info(request):
    #complex data
    ai = Aiquest.objects.all()
    #python dictionary
    serializer = AiquestSerializer(ai, many=True)
    # render Json
    json_data= JSONRenderer().render(serializer.data)
    #Json sent to User
    return HttpResponse(json_data, content_type='application/json')
#Model instance
def aiquest_ins(request, pk):
    #complex data
    ai = Aiquest.objects.get(id=pk)
    #python dictionary
    serializer = AiquestSerializer(ai)
    # render Json
    json_data= JSONRenderer().render(serializer.data)
    #Json sent to User
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def aiquest_create(request):
    if request.method == 'POST':
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        #python to complex data
        serializer = AiquestSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully insert data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        aiq = Aiquest.objects.get(id=id)
        serializer = AiquestSerializer(aiq, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully Updated data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
   
    if request.method == 'DELETE':
        json_data = request.body
        #json to stream convert
        stream = io.BytesIO(json_data)
        #stream to python
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        aiq = Aiquest.objects.get(id=id)
        aiq.delete()
        res = {'msg':'Successfully Deleted data'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')"""