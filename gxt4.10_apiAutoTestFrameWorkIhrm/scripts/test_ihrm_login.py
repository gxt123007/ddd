import unittest

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/" + ".."))

from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import assert_util



'''
import os
# 当前文件的绝对路径,包括文件名
print(__file__)
# 当前文件的系统绝对路径,往往用于添加到环境变量BASE_DIR
print(os.path.abspath(__file__))
# 当前文件所在的目录
print(os.path.dirname(__file__))
# 文件所在目录的上一级目录
print(os.path.dirname(os.path.dirname(__file__)))
# 当前文件所在的目录
print(os.path.dirname(os.path.abspath(__file__)))
'''


class TestIhrmLogin(unittest.TestCase):
    # 登录成功
    def test01_login_success(self):
        # 组织请求数据
        json_data = {"mobile": "13800000002", "password": "123456"}
        # 调用自己封装的接口
        resp = IhrmLoginApi.login(json_data)
        print("登录成功：",resp.json()) 
        # 断言
        assert_util(self,resp,200,True,10000,"操作成功")
        # self.assertEqual(200,resp.status_code)
        # self.assertEqual(True,resp.json().get('success'))
        # self.assertEqual(10000,resp.json().get('code'))
        # self.assertIn("操作成功",resp.json().get('message'))


    # 手机号为空
    def test02_mobile_none(self):
        # 组织请求数据
        json_data = {"mobile": None, "password": "123456"}
        # 调用自己封装的接口
        resp = IhrmLoginApi.login(json_data)
        print("手机号为空：",resp.json())
        # 断言
        assert_util(self,resp,200,False,20001,"用户名或密码错误")
        # self.assertEqual(200,resp.status_code)
        # self.assertEqual(False,resp.json().get('success'))
        # self.assertEqual(20001,resp.json().get('code'))
        # self.assertIn("用户名或密码错误",resp.json().get('message'))

    # 密码错误
    def test03_pwd_err(self):
        # 组织请求数据
        json_data = {"mobile": "13800000002", "password": "1234567890"}
        # 调用自己封装的接口
        resp = IhrmLoginApi.login(json_data)
        print("密码错误：",resp.json())
        # 断言
        assert_util(self,resp,200,False,20001,"用户名或密码错误")
        


if __name__ == "__main__":
    unittest.main()