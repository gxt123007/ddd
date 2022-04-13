import unittest
import requests

from p03_tpshop_login_api import TpshopLoginApi


def commom_assert(self,resp,status_code,status,msg):
    self.assertEqual(status_code,resp.status_code)
    self.assertEqual(status,resp.json().get("status"))
    self.assertIn(msg,resp.json().get("msg"))

class TestTpshopLogin(unittest.TestCase):

    session = None

    @classmethod
    def setUpClass(cls):
        cls.session = requests.Session()
    
    def setUp(self):
        TpshopLoginApi.get_verify(self.session)

    # 测试 登录成功
    def test01_login_ok(self):
        # 创建 session实例

        # 用实例，调用自己封装的 获取验证码 接口
  
        # 调用 自己封装的接口，登录
        login_data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
        resp = TpshopLoginApi.login(self.session,login_data)

        # 断言
        commom_assert(self,resp,200,1,"成功")
 

    # 测试 手机号不存在
    def test02_tel_not_exists(self):
        # 创建 session实例

        # 用实例，调用自己封装的 获取验证码 接口

        # 调用 自己封装的接口，登录
        abc = {"username": "13048932745", "password": "123456", "verify_code": "8888"}
        resp = TpshopLoginApi.login(self.session, abc)

        # 断言
        commom_assert(self,resp,200,-1,"账号不存在")

    # 测试 密码错误
    def test03_pwd_err(self):
        # 创建 session实例

        # 用实例，调用自己封装的 获取验证码 接口

        # 调用 自己封装的接口，登录
        abc = {"username": "13012345678", "password": "123456789", "verify_code": "8888"}
        resp = TpshopLoginApi.login(self.session, abc)

        # 断言
        commom_assert(self,resp,200,-2,"密码错误")
  

if __name__ == "__main__":
    unittest.main()
