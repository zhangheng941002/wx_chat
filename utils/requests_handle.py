import requests
from lxml import etree


def get_handle_etree(target_url):
    # 设置用户代理头
    headers = {
        # 设置用户代理头(为狼披上羊皮)
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    response = requests.get(target_url, headers=headers).content
    resp = etree.HTML(response)
    return resp