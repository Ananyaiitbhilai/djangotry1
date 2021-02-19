from django.http import HttpResponse
from django.shortcuts import render 

def page0(request):
    return render(request,'page0.html')

