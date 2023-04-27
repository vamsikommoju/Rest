from django.contrib import admin
from django.urls import path,include
from app1.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'), 
    path('app1/',include('app1.urls',namespace='app1')), 
]
