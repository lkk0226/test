# coding:utf-8

import unittest
import HTMLTestRunner
import os,sys
import time


current_path = os.getcwd()  # 当前文件路径
print(current_path)
# sys.path.append(current_path)
# PATH = os.environ
#
# for key in PATH:
#     print(key, PATH[key])

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
    # 测试报告为result.html
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    result_path = os.path.join(report_path, now+" result.html")
    # 打开文件，把结果写进文件中，w，有内容的话，清空了再写进去
    fp = open(result_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="测试报告",
                                           description="用例执行情况")
    # 调用all_case函数返回值
    runner.run(all_case())

    # 有开有闭，关闭刚才打开的文件
    fp.close()