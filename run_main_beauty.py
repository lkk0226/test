
import BeautifulReport
from BeautifulReport import BeautifulReport as bf

import unittest
import os
import time

current_path = os.getcwd()  # 当前文件路径
print(current_path)
case_path = os.path.join(current_path, "case")  # 用例路径
print(case_path)
# 存放报告路径
report_path = os.path.join(current_path, "report")
print(report_path)
# discover找出以case开头的用例
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="case*.py")
    print(discover)
    return discover

if __name__ == "__main__":
    runner = bf(all_case()).report(filename='report\\BeautyTest.html', description="登录接口自动化测试")
