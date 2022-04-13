import unittest

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/" + ".."))

from api.ihrm_emp_curd import IhrmEmpCURD
from common.assert_util import assert_util
from common.db_util import DBUtil
from common.read_json_util import read_json_data
from config import TEL

from parameterized import parameterized

from common.get_header import get_header


class TestEmpAddParams(unittest.TestCase):
    # 类属性
    header = None

    @classmethod
    def setUpClass(cls):
        cls.header = get_header()

    def setUp(self) -> None:
        # 删除手机号
        delete_sql = f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.uid_db(delete_sql)

    def tearDown(self) -> None:
        # 删除手机号
        delete_sql = f"delete from bs_user where mobile = '{TEL}'"
        DBUtil.uid_db(delete_sql)

    # 通用测试方法 - 实现参数化
    path_filename = "./data/add_emp.json"
    @parameterized.expand(read_json_data(path_filename))
    def test_add_emp(self, desc, json_data, stauts_code, success, code, message):
        # 调用自己封装的 接口
        resp = IhrmEmpCURD.add_emp(self.header, json_data)
        print(desc, "：", resp.json())

        # 断言
        assert_util(self, resp, stauts_code, success, code, message)

if __name__ == '__mian__':
    unittest.main()