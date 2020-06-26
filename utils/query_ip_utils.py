from pypinyin import lazy_pinyin

from utils.settings import city_dict, province_dict

from utils.requests_handle import get_handle_etree


# 查询ip归属地
def query_ip_attribution(ip_addr):
    target_url = "http://www.ip138.com/ips138.asp?ip=" + ip_addr
    data_etree = get_handle_etree(target_url)
    ip_attr = data_etree.xpath('//tr[3]/td/ul/li[1]//text()')
    ip_attr1 = data_etree.xpath('//tr[3]/td/ul/li[2]//text()')
    ip_attr2 = data_etree.xpath('//tr[3]/td/ul/li[3]//text()')
    ip_att = ip_attr[0].strip("本站数据：")
    ip_att1 = ip_attr1[0].strip("参考数据1：")
    ip_att2 = ip_attr2[0].strip("参考数据2：")
    return {"ip": ip_addr, "ip_attr": ip_att, "data1": ip_att1, "data2": ip_att2}


# 查询电脑出网IP
def query_your_own_ip():
    target_url = "http://www.net.cn/static/customercare/yourip.asp"
    data_etree = get_handle_etree(target_url)
    ip_attr = data_etree.xpath('//h2//text()')
    return {"ip": ip_attr[0]}


if __name__ == '__main__':
    # print(query_ip_attribution("114.112.84.198"))

    ip = query_your_own_ip()
    print(ip)
    # info = query_ip_attribution(ip)
    # print(info)
