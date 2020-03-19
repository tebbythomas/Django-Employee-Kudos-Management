from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/employees', views.upload_employees, name='upload_employees'),
    path('upload/kudos', views.upload_kudos, name='upload_kudos'),
]
