from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Pulasthi'})

def add(request):
    
    val1 = float(request.POST['num1'])
    val2 = float(request.POST['num2'])
    res = val1 + val2

    return render(request,'result.html',{'result':res})