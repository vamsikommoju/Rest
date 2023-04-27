from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('courses/<int:pk>',views.courseinfo,name='courseinfo'),
    path('courses',views.courses,name='courses'),
]
