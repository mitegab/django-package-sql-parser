import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.core.serializers import serializer

# Create your views here.

def home(request):
    qs = Product.objects.all()
    serialized_data =serializer('json', qs)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, status=200)

    
