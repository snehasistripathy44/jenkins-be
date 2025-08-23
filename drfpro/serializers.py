from rest_framework import serializers
from drfpro.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    # def validate_age(self,value):
    #     if value>=61:
    #         raise serializers.ValidationError("Age can not be greaterthan 60 or more")
    #     return value
        
    # def validate(self,data):
    #     if data.get("ename").lower() == "snehasis":
    #         raise serializers.ValidationError("name cannot be snehasis")
    #     if data.get("age")>=61:
    #         raise serializers.ValidationError("agemust be lessthan 60")
    #     if data.get("addr") == "pakistan":
    #         raise serializers.ValidationError("pakistan employee are nopt eligible to job")
    #     return data 


    # eno = serializers.IntegerField()
    # ename = serializers.CharField(max_length=50)
    # age = serializers.IntegerField()
    # addr = serializers.CharField(max_length=50)
    # cname = serializers.CharField(max_length=50)
    
    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.eno = validated_data.get("eno",instance.eno)
    #     instance.ename = validated_data.get("ename",instance.ename)
    #     instance.age = validated_data.get("age",instance.age)
    #     instance.addr = validated_data.get("addr",instance.addr)
    #     instance.cname = validated_data.get("cname",instance.cname)
    #     instance.save()
    #     return instance