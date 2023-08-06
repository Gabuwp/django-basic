
from django.contrib import admin
from django.urls import path
from home import views as index_views

app_name = "home"

urlpatterns = [
    path('', index_views.index,name="index")
]
