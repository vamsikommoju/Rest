from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('courses',views.courses,name='courses')
]
