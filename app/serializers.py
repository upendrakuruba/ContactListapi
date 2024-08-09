from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'