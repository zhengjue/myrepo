# _*_ coding:utf-8  _*_
from django.shortcuts import render, render_to_response,HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','PUT','DELETE','POST'])
def servers(request):
    method = request.method
    if method == 'POST':
        pass
    #  return HttpResponse("dddd")
    return Response("dddd")



def index(request):
    return render_to_response("index.html")

def userlist(request):
    return render_to_response("userlist.html")


def login(request):
    return render_to_response("login.html")

