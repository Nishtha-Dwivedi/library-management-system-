
from copyreg import add_extension
from django.http import HttpResponse
from django.shortcuts import redirect, render
from socialmedia.models import Library
from django.contrib import messages
# Create your views here.

from socialmedia.models import Register
from socialmedia.models import Loginn
from socialmedia.models import admin_login

def register(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        UserName=request.POST.get('UserName')
        password=request.POST.get('password')
        ConfirmPassword=request.POST.get('ConfirmPassword')

        register=Register(name=name,email=email,UserName=UserName,password=password,ConfirmPassword=ConfirmPassword)
        if password==ConfirmPassword:
         register.save()
         
        else:
            messages.error(request,"Password do not match")
    
    return render(request,'register.html')
def login(request):
   if request.method=='POST':
       UserName=request.POST.get('UserName')
       password=request.POST.get('password')
       
       if UserName=='nishtha' and password=='12345':
           return redirect('/home')
       registrations=Register.objects.get(UserName=UserName,password=password)

      
       if registrations:
           logins=Loginn(UserName=UserName,password=password)
           logins.save()
           return redirect('/show')
           

   
   return render(request,'login.html')


def home(request):
    if request.method=='POST':
        bookId=request.POST.get('bookId')
        bookName=request.POST.get('bookName')
        authorName=request.POST.get('authorName')
        price=request.POST.get('price')

        # library1=Library(bookId=bookId)
        # if library1:
        #     redirect("/home")
        # else:
        library=Library(bookId=bookId,bookName=bookName,authorName=authorName,price=price)
        library.save()


    return render(request,'home.html')
def display(request):
    libraries=Library.objects.all()
    return render(request,'display.html',{'libraries':libraries})   

def show(request):
    libraries=Library.objects.all()
    return render(request,'show.html',{'libraries':libraries})   

def discard(request,bookId):
    library=Library.objects.get(bookId=bookId)
    library.delete()
    return redirect("/display")

def edit(request,bookId): 
    
    library=Library.objects.get(bookId=bookId)

    return render(request,'edit.html',{'library':library})
def update(request,bookId):
    
    library=Library.objects.get(bookId=bookId) 
    library.bookId=request.POST.get('bookId')   
    library.bookName=request.POST.get('bookName')
    library.authorName=request.POST.get('authorName')
    library.price=request.POST.get('price')
    
    library.save()
    return redirect('/display')   
