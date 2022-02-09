import email
from importlib.resources import contents
from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse 
import cv2
from flask import request
import numpy as np
from shop.models import bloghome, contact, prod
def home(request):    
    if request.method=="POST":    
        ob=request.POST['a']
        obj=request.POST['b']
        obj4=request.POST['c']
        o=request.POST['d']

        if obj=="":
            pass
        else:

            blogo=bloghome(content=obj,title=ob,name=obj4,slu=o)
            blogo.save()
    return render(request,'homeshop.html')

def about(request):
    #ill take a variable which will take all the objects of the blohome database class
    var=bloghome.objects.all()

    """var will be holding
    var{blohhome.ttile
    content , name } of each table db
    
     now var goes to (la) """
    #rendertakes a dictonray in html orm apge so i need to build a dict nmae anythong
    kar={'la':var}

    return render(request,'about.html',kar)

    
def ok(request):
    if request.method=="POST":
        obj1=request.POST['obj1']
        
        obj2=request.POST['obj3']
        if obj1=="" or obj2=="":
            pass
        else:
        #here i made an object of contact class
            con=contact(content=obj1,email=obj2)
            con.save()
    return render(request,'ok.html')


def blogposts(request,slu):
    blbl=bloghome.objects.filter(slu=slu).first()
    print(blbl)
    dictonary={'lp':blbl}
    return render(request,'blogshow.html',dictonary)

def calc(request):

    d=eval(request.POST['di1'])
    c=eval(request.POST['di2'])
    s=d+c
    print(c)
    return render(request,'homeshop.html',{'s':s})


def search(request):
    value=request.POST['id2']
    sir={}
    if value=="":
        pass
    else:  
        sir={'var':bloghome.objects.filter(title__icontains=value)}

    return render(request,'search.html',sir)


def product(request):
    var={}
    if request.method=="POST":
        a=request.POST['dim1']
        b=request.POST['dim2']
        sal=prod.objects.filter(botlength__icontains=a)
        nal=prod.objects.filter(botdiameter__icontains=b)
    
      
        var={'sal':sal,'nal':nal}
            

    return render(request,'myproduct.html',var)

    
def page(request):
    return render(request,'page.html')



















