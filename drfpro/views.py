from django.shortcuts import render
from drfpro.models import *
from rest_framework.viewsets import ModelViewSet
from drfpro.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class Curdapi(ModelViewSet):
    def addpost(self,request):
        data = request.data
        siri_obj = EmployeeSerializer(data = data)
        if siri_obj.is_valid():
            siri_obj.save()
            return Response(siri_obj.data,status=status.HTTP_200_OK)
        else:
            return Response(siri_obj.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def getemp(self,request):
        qs = Employee.objects.all()
        serialized_data = EmployeeSerializer(qs,many = True)
        data = serialized_data.data
        return Response(data,status=status.HTTP_200_OK)

    def updatename(self,request,pk):
        data = request.data
        print(pk)
        qs = Employee.objects.get(eno = pk)
        print(qs.eno)
        esiri = EmployeeSerializer(qs,data)
        if esiri.is_valid():
            esiri.save()
        return Response(esiri.data,status=status.HTTP_202_ACCEPTED)
    
    def patchemployee(self,request,pk):
        data = request.data
        # qs = Employee.objects.update_or_create(defaults=data)

        # esiri = EmployeeSerializer(qs,data = data)
        # if esiri.is_valid():
        #     esiri.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class Curdapiview(ModelViewSet):
    def get(self,request):
        qs = Employee.objects.filter().values()
        #snehasis
        return Response(qs,status=status.HTTP_200_OK)
        
    
