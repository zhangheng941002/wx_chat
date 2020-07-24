from django.core import serializers
import json


def show_page(page, queryset, step):
    # 每页显示条数
    import math
    total_page_num = math.ceil(len(queryset) / step)
    if page >= total_page_num:
        page = total_page_num
    elif page <= 0:
        page = 1
    if page != total_page_num:
        res = json.loads(serializers.serialize('json', queryset[(page - 1) * step: (page - 1) * step + step]))
    else:
        if len(queryset) % step == 0:
            res = json.loads(serializers.serialize('json', queryset[(page - 1) * step: (page - 1) * step + step]))
        else:
            step1 = len(queryset) % step
            res = json.loads(serializers.serialize('json', queryset[(page - 1) * step: (page - 1) * step + step1]))
    return res