import requests
from requests import HTTPError


def getLogin():
    url = url = "https://javaapi.tepleton.info/api/v1/login"
    headers = {
        "Content-Type": "application/json"
    }
    date = {
        "phone": "13072373333", "password": "123456aa", "smsCode": "111"
    }

    res = requests.post(url, headers=headers, json=date)
    #  response = requests.post(url=url, headers=headers,json=data)将date字段转换为json字段

    token = res.json()["data"]["token"]
    # 返回JSON中data数据的token
    # print(res.json())
    return token


def getPrize():
    headers = {
        "Authorization": getLogin(),
    }
    url = "https://javaapi.tepleton.info/api_game/api/v1/product/prize/app/prize"
    getPrizes = requests.post(url, headers=headers)
    print(getPrizes.url)
    print(getPrizes.text)
    # Prize=getPrizes.json()["data"]["name"]
    # print(Prize)
    # 服务器返回状态码在200-400之间，打印Success。
    if getPrizes:
        print('Success!')
    else:
        print('An error has occurred.')


'''
不检查服务响应的状态码，请求失败就拋出一个异常
如果在处理过程中发生错误，则response.raise_for_status()返回HTTPError对象。
它用于调试请求模块，并且是Python请求的组成部分。
Python请求通常用于从特定资源URI中获取内容。每当我们通过Python向指定URI发出请求时，
它都会返回一个响应对象'''


def sendError():
    for url in ['https://www.baidu1.com', 'https://www.bilibilii.com/v/life/']:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'Http error occurred:{http_err}')
        except Exception as err:
            print(f'Other error occurred:{err}')
        else:
            print('Success')


def getRequestCase():
    # 以一个字符串字典来提供这些参数
    payload = {
        "aid": 2608,
        "not_self": 0
           }
    r = requests.get("https://apinew.juejin.im/user_api/v1/user/get", params=payload)

    # 将一个列表作为值传入
    payload = {
        "aid": [2680, 2789],
        "not_self": 0

    }
    re = requests.get("https://apinew.juejin.im/user_api/v1/user/get", params=payload)
    #  以字符串格式查看响应的内容
    print(re.text)
    print(re.json())
    # .json() 返回值的类型是字典类型，因此你可以使用键值对的方式访问对象中的值。
getRequestCase()