from pypinyin import lazy_pinyin

from utils.settings import city_dict, province_dict

from utils.requests_handle import get_handle_etree


def query_province():
    """
    返回省份直辖市
    :return:
    """
    target_url = "http://qq.ip138.com/weather/search.asp"
    data_etree = get_handle_etree(target_url)
    province = data_etree.xpath('//table[@class="t12"]//tr//td/a//text()')
    return province


def chinese_to_py(chinese):
    t = lazy_pinyin(chinese)
    pyin = "".join(t)
    return pyin


def query_city(province):
    """
    返回省份或者直辖市下的城市或区
    :param province: 省份/直辖市中文
    :return:
    """

    pyin = chinese_to_py(province)
    target_url = "http://qq.ip138.com/weather/{}/".format(pyin)
    data_etree = get_handle_etree(target_url)

    # 省份
    city = data_etree.xpath('//table[@class="t12"]//tr//td/a//text()')
    if not city:
        # 直辖市
        city = data_etree.xpath('//table[@class="t3"]//tr//td/a//text()')
    return city


# 查询天气
def query_weather(city):
    province = ""
    for k, v in city_dict.items():
        if k == city:
            province = province_dict.get(v)
            break
    if city in ["北京", "上海", "重庆", "天津"]:
        target_url = "http://qq.ip138.com/weather/{city}/".format(city=chinese_to_py(city))
    else:
        if not province:
            return {"status": 0, "city": city, "date": [], "weather": [], "temperature": [], "wind": []}
        target_url = "http://qq.ip138.com/weather/{province}/{city}.htm".format(province=province,
                                                                                city=chinese_to_py(city))
    data_etree = get_handle_etree(target_url)
    resp = data_etree.xpath('//body/table//tr//td//text()')
    response = {
        "status": 1,
        "city": city
    }

    if city in ["北京", "上海", "重庆", "天津"]:
        date = resp[26:31]
        weather = resp[31:36]
        temperature = resp[36:41]
        wind = resp[41:46]
        response["date"] = date
        response["weather"] = weather
        response["temperature"] = temperature
        response["wind"] = wind
    else:
        date = resp[28:33]
        weather = resp[33:38]
        temperature = resp[38:43]
        wind = resp[43:48]
        response["date"] = date
        response["weather"] = weather
        response["temperature"] = temperature
        response["wind"] = wind
    return response


if __name__ == '__main__':

    w = query_weather("上海")
    print(w)
    print(chinese_to_py("睡懒觉"))
