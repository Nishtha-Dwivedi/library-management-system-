from django.db import models

# Create your models here.
class Library(models.Model):
  bookId=models.CharField(max_length=10)
  bookName=models.CharField(max_length=50)
  authorName=models.CharField(max_length=50)
  price=models.CharField(max_length=10)


class Loginn(models.Model):
  UserName=models.CharField(max_length=50)
  password=models.CharField(max_length=10)

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    UserName=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    ConfirmPassword=models.CharField(max_length=20)

class admin_login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=10)   

class adminlogin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=10)   