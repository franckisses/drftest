from django.shortcuts import render
from rest_framework.settings import api_settings
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response 
# Create your views here.


class Index(APIView):

    def get(self,request):
        print(request)
        print(request.data,type(request.data))
        print(request.query_params['name'])
        return Response({'code':200})

    def post(self,request):
        print(request.data,type(request.data))
        print(request.query_params)
        return Response({'code':200})


