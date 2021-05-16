from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def title(request,name):
    return HttpResponse('<h1>Hi! {}</h1>'.format(name))
