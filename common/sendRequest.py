import unittest
import requests
import json

from common.readExcel import ReadExcel
from common.writeExcel import WriteExcel


class SendRequests:
    def sendRequests(apidata, filename):
        rownumber = apidata['rownum']
        casename = apidata['casename']
        method = apidata['method']
        url = apidata['url']
        head = apidata['hearder']
        if type(head)==dict:
            head_dict = head
        else:
            head_dict = json.loads(head)
        if 'param' in apidata.keys():
            param = apidata['param']
        else:
            param = None
        expectRes = apidata['expectRes']

        print("*******正在执行用例%s：%s**********" % (rownumber, casename))
        res = {}
        if method == 'post':
            if param==None:
                response = requests.post(url=url, headers=head_dict)
            else:
                print("post请求%s %s" % (url,param))
                response = requests.post(url=url, data=param, headers=head_dict)
        elif method == 'get':
            if param==None:
                response = requests.get(url=url, headers=head_dict)
            else:
                response = requests.get(url=url, data=param, headers=head_dict)
        else:
            print("不是post和get请求")

        #print("响应值=", response.text)
        headers_str = json.dumps(dict(response.headers))
        headers_dict = json.loads(headers_str)
       # print(type(headers_dict))

        if 'x-auth-token' in headers_dict.keys():
            token = headers_dict['x-auth-token']
            head_dict["x-auth-token"] = token
            res['head'] = head_dict
        else:
            res['head'] = head_dict

        res['rownumber'] = rownumber
        res['status_code'] = response.status_code
        res['content'] = response.content.decode("utf-8")
        if res["status_code"] != 200:
            res['error'] = res['content']
        else:
            res['error'] = ""

        if response.text == expectRes:
            res['result'] = "pass"
        else:
            res['result'] = "fail"
        print("res=", res)
        return res


    def write_result(result, filename):
        row_nub = result['rownumber']
       #print("row_nub=", row_nub)
        wt = WriteExcel(filename)
        wt.writeExcel(row_nub, 8, result['status_code'])
        wt.writeExcel(row_nub, 9, result['error'])
        wt.writeExcel(row_nub, 10, result['result'])

    def update_listapi(listapidata,dictdate):
        for i in range(0, len(listapidata)):
            print("i=", i)
            listapidata[i]['hearder'] =json.dumps(dictdate)
           # print ("listapi=", listapidata[i])


if __name__ == '__main__':
    listdate = ReadExcel.readExcel("F:\\pythonPjo\\testExcelCase\\data\\login.xlsx","test")[0]
    print("listdate=", listdate)
    res_data = SendRequests.sendRequests(listdate, "F:\\pythonPjo\\testExcelCase\\data\\login.xlsx")
    print("res_data=", res_data)
    SendRequests.write_result(res_data, "F:\\pythonPjo\\testExcelCase\\data\\login.xlsx")

    if 'x-auth-token' in res_data['head'].keys():
        SendRequests.update_listapi(listdate, res_data['head'])
    print("更新后的listdate=",listdate)












