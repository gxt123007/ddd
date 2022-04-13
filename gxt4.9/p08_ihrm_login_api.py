# 接口对象层
import requests


class IhrmLoginApi(object):
    @classmethod
    def login(cls, json_data):
        resp = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json=json_data)
        return resp


if __name__ == "__main__":
    data = {"mobile": "13800000002", "password": "123456"}
    resp = IhrmLoginApi.login(data)    
    print(resp.json())