from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def sample_fun(req):
    d=project_user.objects.all()
    s=sample(d,many=True)
    return JsonResponse(s.data,safe=False)
@csrf_exempt
def mode_view(req):
    if req.method=='GET':
      d=project_user.objects.all()
      s=model_serializer(d,many=True)
      return JsonResponse(s.data,safe=False)
    elif req.method=='POST':
       d=JSONParser().parse(req)
       s=model_serializer(data=d)
       if s.is_valid():
          s.save()
          return JsonResponse(s.data)
       else:
          return JsonResponse(s.errors)