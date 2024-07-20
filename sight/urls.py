from django.urls import path

from sight.views import sight_list

urlpatterns = [
    path('sight_list', sight_list, name='sight_list')
]