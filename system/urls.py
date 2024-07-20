from django.urls import path
from .views import slider_list

urlpatterns = [
    path('slider_list', slider_list , name='slider_list'),
]
