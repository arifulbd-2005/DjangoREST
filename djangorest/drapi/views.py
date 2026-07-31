from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class Aiquest_List_Create(ListCreateAPIView):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

class Aiquest_Retrieve_Update_Destroy(RetrieveUpdateDestroyAPIView):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    
"""# sortcut ModelMixin................................
from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# Create your views here.
class Aiquest_List_Create(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Aiquest_Retrieve_Update_Destroy(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)"""

    
"""#ListModelMixin.................................

from .models import Aiquest
from .serializers import AiquestSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# Create your views here.
class AiquestList(GenericAPIView, ListModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class AiquestCreate(GenericAPIView, CreateModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AiquestRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class AiquestUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class AiquestDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Aiquest.objects.all()
    serializer_class = AiquestSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)"""


"""# Class based views....................

from django.shortcuts import render
import rest_framework
from .models import Aiquest
from.serializers import AiquestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AiquestCreate(APIView):
    def get(self, request, pk=None, format=None):
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
    def post(self, request, format=None):
        serializer = AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully insert data'})
        return Response(serializer.errors)
    def put(self, request, pk, format=None):
        id = pk
        #complex data
        ai = Aiquest.objects.get(id=id)
        #python dictionary
        serializer = AiquestSerializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully Full data Updated'})
        return Response(serializer.errors)
    def patch(self, request, pk, format=None):
        id = pk
        ai = Aiquest.objects.get(id=id)
        serializer = AiquestSerializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully partial data Updated'})
        return Response(serializer.errors)
    def delete(self, request, pk, format=None):
        id = pk
        ai = Aiquest.objects.get(id=id)
        ai.delete()
        return Response({'msg':'Successfully Deleted data'})"""


# Function based views.................

"""from django.shortcuts import render
from .models import Aiquest
from.serializers import AiquestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
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

    if request.method == 'POST':
        serializer = AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully insert data'}
            return Response(res)
        return Response(serializer.errors)


    if request.method == 'PUT':
        id = pk
        #complex data
        ai = Aiquest.objects.get(id=id)
        #python dictionary
        serializer = AiquestSerializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully Full data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = pk
        ai = Aiquest.objects.get(id=id)
        serializer = AiquestSerializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully partial data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = pk
        ai = Aiquest.objects.get(id=id)
        ai.delete()
        return Response({'msg':'Successfully Deleted data'})"""



# 3rd party APP based views....................

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