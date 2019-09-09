from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Persons
from rest_framework.permissions import IsAuthenticated
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
