from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect


def home(request):
    return HttpResponseRedirect("shop/home")

def about(request):
    return render(request,'about.html')
   
def service(request):
    return HttpResponse('this is service')    


