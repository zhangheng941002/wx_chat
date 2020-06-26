import urllib.parse
import http.client
import random
import hashlib

# 通过在http://ai.youdao.com/ 执行以下操作获取
# 1.注册账号 => 2.创建应用 => 3.创建实例 => 4.应用绑定对象
# appKey = '784ece665fa5e907'
# secretKey = 'Ap2IyfAaaDUryMR4Q7l8u73ZGoC9vOSZ'

# 自己的
appKey = '720fcb6de30caf7a'
secretKey = 'dClXe1TGlfXD9o4xEqnjfo27aFplKBrR'


# 中译英
def Ch2En(item):
    httpClient = None
    myurl = '/api'

    fromLang = 'zh-CHS'  # 译文主体
    toLang = 'EN'  # 译文客体

    salt = random.randint(1, 65536)
    sign = appKey + item + str(salt) + secretKey
    m1 = hashlib.new('md5')
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()

    # 拼接完整译文对象
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(
        item) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    result = ""
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result = eval(response.read().decode("utf-8"))['translation']
        # print(type(result))
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return result


# 英译中
def En2Ch(item):
    httpClient = None
    myurl = '/api'

    fromLang = 'EN'  # 译文主体
    toLang = 'zh-CHS'  # 译文客体

    salt = random.randint(1, 65536)
    sign = appKey + item + str(salt) + secretKey
    m1 = hashlib.new('md5')
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(
        item) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    result = ""
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result = eval(response.read().decode("utf-8"))['translation']

    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return result


if __name__ == '__main__':
    c2e = Ch2En('完美的一天')
    print("Ch2En:", c2e[0])
    e2c = En2Ch(c2e[0])
    print("En2Ch:", e2c[0])
