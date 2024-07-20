from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from sight.models import Sight


# Create your views here.
def sight_list(request):
    is_hot = request.GET.get('is_hot', None)
    is_star = request.GET.get('is_star', None)

    query = Q(is_valid=1)

    # 1、热门景点搜索
    if is_hot:
        query = query & Q(is_hot=1)
    # 2、精选景点搜索
    if is_star:
        query = query & Q(is_star=1)
    # 3、TODO：根据标题搜索
    queryset = Sight.objects.filter(query)

    # 分页
    per_page_count = 5
    page_index = 1

    p = Paginator(queryset, per_page_count)
    total_pages = p.num_pages
    total_count = p.count
    page = p.page(page_index)

    print('page', page)

    data = {
        'meta': {
            'total_count': total_count,
            'total_pages': total_pages,
            'per_page_count': per_page_count,
            'page_index': page_index,

        }, 'objects': []
    }

    for item in page:
        data['objects'].append(
            {
                'id': item.id,
                'name': item.name,
                'img': item.img.url,
                'score': item.score,
                'comment_count': item.comment_count,
                'province': item.province,
                'city': item.city,
            }
        )

    return JsonResponse(data)
