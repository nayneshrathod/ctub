from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        "sample": "My Tilels"
    }
    return JsonResponse(data={"data": data})
