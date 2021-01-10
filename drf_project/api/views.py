import json
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response

WEATHERMODES = ["rainy", "cloudy", "shiny", "tornado!", "snow"]

# Example api view

@api_view(http_method_names=['GET'])
def get_weather(request):

    temp = random.randint(-5, +25)
    weather = random.choice(WEATHERMODES)
    humidity = random.randint(30, 90)

    return Response({"temp": temp, "weather": weather, "humidity": humidity})



@api_view(http_method_names=['POST'])
def add_request(request):
    request_data = request.data

    with open("data_file.json", "w") as write_file:
        json.dump(request_data, write_file)

    return Response({})
