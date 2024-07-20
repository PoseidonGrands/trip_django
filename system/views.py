from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from system.models import Slider


# Create your views here.

def slider_list(request):
    """轮播图接口"""
    data = {
        'meta': {

        },
        'objects': [

        ]
    }
    sliders = Slider.objects.filter(is_valid=1)
    for item in sliders:
        data['objects'].append({
            'id': item.id,
            'name': item.name,
            'desc': item.desc,
            'img': item.img.url,
            'target_url': item.target_url,
            'types': item.types,
            'reorder': item.reorder,
            'start_time': item.start_time,
            'end_time': item.end_time,
        })

    return JsonResponse(data)
