def show_page_list(page, lists, step):
    # 每页显示条数
    import math
    total_page_num = math.ceil(len(lists) / step)
    if page >= total_page_num:
        page = total_page_num
    elif page <= 0:
        page = 1
    if page != total_page_num:
        res = lists[(page - 1) * step: (page - 1) * step + step]
    else:
        if len(lists) % step == 0:
            res = lists[(page - 1) * step: (page - 1) * step + step]
        else:
            step1 = len(lists) % step
            res = lists[(page - 1) * step: (page - 1) * step + step1]
    return res