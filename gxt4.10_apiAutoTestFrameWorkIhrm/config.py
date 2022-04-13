"""
存放 全局变量
"""
# 全局手机号
TEL = "13900043762"

import os
# 全局 项目目录
BASE_DIR = os.path.dirname(__file__)  # 获取 当前文件的 上一级 目录（文件夹） 的路径
print(BASE_DIR)


# print("__file__:",__file__)   __file__ 获取 当前文件的 绝对路径