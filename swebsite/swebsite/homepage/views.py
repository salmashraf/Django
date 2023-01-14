from django.http import HttpResponse
from django.shortcuts import render
from .models import Books
from django.conf import settings
# from django.http import HttpResponse, render 
# Create your views here.

def pagesIndex(request):
    {"user":"salma"}
    list_of_users=[{"Name":"Ahmed","Age":"25","Salary":"12 K"},{"Name":"Omar","Age":"30","Salary":"23 K"},{"Name":"Mona","Age":"45","Salary":"40 K"}]
    dict={"users":list_of_users}
    return render(request,'homepage/salma.html',dict)
    #HttpResponse("Hello from views.py of homepage")
    
def viewBooks(request):
    return render(request,'homepage/books.html', {"Books":Books.objects.all()})    

def homepageAbout(request):
    return HttpResponse ("Hello from about")

