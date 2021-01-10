import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

USERNAME = "Sir Grover Robinson"
OPTIONS = ["Python", "Java", "C", "Kotlin"]


# Example api view

@api_view(http_method_names=['GET'])
def get_username(request):
    return Response({"full_name": "Colleen Mirela"})


@api_view(http_method_names=['GET'])
def get_options(request):
    return Response(OPTIONS)


@api_view(http_method_names=['POST'])
def add_request(request):
    request_data = request.data

    with open("data_file.json", "w") as write_file:
        json.dump(request_data, write_file)

    return Response({})
