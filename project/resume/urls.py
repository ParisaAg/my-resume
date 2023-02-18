from django.urls import path
from django.contrib import admin
from . import views
from resume.views import *


urlpatterns = [
path('',views.index,name='index'),
path('test',views.test,name='test'),
path('form',views.form,name='form'),

]