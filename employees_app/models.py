from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    dept  = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    join_date = models.DateTimeField(auto_now_add=True)
    image     = models.ImageField(upload_to='Employee/images')

class Profession(models.Model):
    name  =  models.CharField(max_length=23, unique=True)


# user profile model here extend
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio  = models.TextField(default='Write details/description about your self. Like you can also describe your past experiences as well',   max_length=500)
    pic  = models.ImageField(default='static/images/user.png'  ,upload_to='Profile/images')
    address = models.CharField(max_length=78)


# model for api as Employee mode
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=50)
    age   = models.IntegerField()
    salary     = models.IntegerField()