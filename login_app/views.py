from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from .serializers import UserSerializer
from rest_framework import viewsets,permissions,status
from rest_framework.decorators import api_view
from .models import Persons
from rest_framework.response import Response
    
class NewUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self,request):
        if request.method=='POST':
            try:
                username = request.data['username']
                password = request.data['password']
                user = User.objects.create_user(username=str(username),password=str(password))
                return Response(request.data,status.HTTP_201_CREATED)
            except Exception as e:
                return Response(e.args,status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request):
        if request.method=='GET':
            pass