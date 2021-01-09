from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

USERNAME = "Sir Grover Robinson"
OPTIONS = ["Python", "Java", "C", "Kotlin"]

# Basic html view

def sample_view(request):
   context = {}
   return render(request, 'index.html', context=context)

# Example api view

@api_view(http_method_names=['GET'])
def sample_get_username(request):
    return Response({"status":"ok"})

@api_view(http_method_names=['GET'])
def sample_get_options(request):
    return Response(OPTIONS)\

@api_view(http_method_names=['POST'])
def sample_add_request(request):
    request_data = request.data

    with open("data_file.json", "w") as write_file:
        json.dump(request_data, write_file)

    return Response({})