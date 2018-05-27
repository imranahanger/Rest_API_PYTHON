from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from webapp.models import employees
from . serializers import employeesSerializers


class employeeList(APIView):

    def get(self,request):
        employees1 = employees.objects.all()
        serializer = employeesSerializers(employees1, many = True)
        return Response(serializer.data)
    def post(self,request):
        print(self)
        return Response({'a':2})