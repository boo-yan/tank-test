import requests

'''params = {"chainName":"eth",
              "address":"0x126cd49a00e7db25a35f2e74269ab3943319bc6c",
              "page":"1",
              "pageSize":"200",
              "adressType":"3"

    }
    url = "https://explorer.tepleton.info/api/v1/transaction?"
    '''
# 查询余额


def getLogin():
    url = url = "https://javaapi.tepleton.info/api/v1/login"
    headers = {
        "Content-Type": "application/json"
    }
    date = {
        "phone": "13072378888", "password": "123456aa", "smsCode": "111"
    }

    res = requests.post(url=url, headers=headers, json=date)
    #  response = requests.post(url=url, headers=headers,json=data)将date字段转换为json字段

    print(res.status_code)
    #  返回响应头
    print(res.text)
    #  返回响应信息
    return (res.json()["date"]["token"])

def getPrize():

    url="https://javaapi.tepleton.info/api_game/api/v1/product/prize/app/prize"

getLogin()
