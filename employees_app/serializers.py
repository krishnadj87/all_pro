
from rest_framework import serializers
from .models import Student

# StudentSerializer class
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Student
        fields = ('name','age', 'salary', 'email')
