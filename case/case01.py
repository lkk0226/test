# coding:utf-8


import unittest
import requests
import json
import HTMLTestRunner
from ddt import ddt, data, unpack
from common.readExcel import ReadExcel
from common.sendRequest import SendRequests


testdata = ReadExcel.readExcel("F:\\pythonPjo\\testExcelCase\\data\\login.xlsx", "test")
#print("testdate=", testdata)

@ddt
class excelTest(unittest.TestCase):
    def setUp(self):
        print('开始接口测试')

    def tearDown(self):
        print('完成接口测试')

    @data(*testdata)
    #@unpack
    def test_login(self, data):
        """登录"""
        r = SendRequests.sendRequests(data, "F:\\pythonPjo\\testExcelCase\\data\\login.xlsx")
        SendRequests.write_result(r, "F:\\pythonPjo\\testExcelCase\\data\\login.xlsx")
        expectRes = data['expectRes']
        # print("data[header]",data['hearder'])
        # print("data[header]", type(data['hearder']))
        self.assertEqual(json.loads(expectRes).get("desc"), json.loads(r['content']).get("desc"))
        if 'x-auth-token' in r['head'].keys():
            SendRequests.update_listapi(testdata, r['head'])
        print("更新后的listdate=", testdata)

if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
    # test_suit = unittest.TestSuite()
    # test_suit.addTest(unittest.makeSuite(excelTest))
    # report_path = "Res.html"
    # fp = open(report_path, "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(fp, title="aaa", description="bbb")
    # runner.run(test_suit)