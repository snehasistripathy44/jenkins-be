from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_age(value):
    if value>60:
        raise ValidationError("age must be lessthan 60")
def validate_ename(value):
    if value.isalpha() == False:
        raise ValidationError("name must be alphabet")
def validate_eno(value):
    if value not in range(100,200):
        raise ValidationError("eno must be in 100,200")


class Employee(models.Model):
    eno = models.IntegerField(validators=[validate_eno])
    ename = models.CharField(max_length=50,null=True,blank=True,validators=[validate_ename,])
    age = models.IntegerField(validators=[validate_age,])
    addr = models.CharField(max_length=50,null=True,blank=True)
    cname = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        db_table = "employee"

    
