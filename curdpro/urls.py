"""
URL configuration for curdpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drfpro.views import *                                                                        

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addpost',Curdapi.as_view({"post":"addpost"})),       
    path('getemp',Curdapi.as_view({"get":"getemp"})),
    path('updatename/<int:pk>',Curdapi.as_view({"put":"updatename"})),
    path('patchemployee/<int:pk>',Curdapi.as_view({"patch":"patchemployee"})),\
    path('get',Curdapiview.as_view({"get":"get"})),       
    

]