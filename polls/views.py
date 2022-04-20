from django.http import HTTPResponse
from django.shortcuts import render

def index(request):
    return HTTPResponse("Hello, Django!")

# Create your views here.
