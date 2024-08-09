from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework import permissions
# Create your views here.

class Slist(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes =(permissions.IsAuthenticated,)
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    

class Sretrieve(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class =StudentSerializer
    permission_classes =(permissions.IsAuthenticated,)
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    
    def delete(self,request,**kwargs):
        return self.destrory(request,**kwargs)
    
