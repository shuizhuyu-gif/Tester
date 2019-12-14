# -*- coding: UTF-8 -*-
#-*-coding:GBK -*-
import unittest
import requests
import json
import sys
sys.path.append("../..")  #到主目录下
from Objectd.Tester.config.config import *
from Objectd.Tester.tools.read_data import *
# from Objectd.Tester.tools.log_case import *
from Objectd.Tester.tools.log_case import log_case_info

class Testlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  #测试类，执行一次
        cls.data_list = excel_data_list(os.path.join(data_path,"test_data.xlsx"),"login")
        #data_list 同 self.data_list 都是该类的公共属性

    def test_login_normal(self):
        case_data = get_test_data(self.data_list,"test_login_normal")
        if not case_data:
            logging.error("未找到该用例数据！")

            url = case_data.get("URL")  #excel中对应数据
            data = case_data.get("data")    #注意字符串格式,转换格式
            expect_data = case_data.get("expect_data")   #期望数据

            requested = requests.post(url=url,data = json.loads(data))
            log_case_info("test_login_normal",url,data,expect_data,requested.text)
            self.assertEqual(requested.text,expect_data)   #断言

    def test_login_wrong(self):
        case_data = get_test_data(self.data_list,"test_login_wrong")   #在数据列表中查找用例数据
        if not case_data:
            logging.error("未找到该用例数据")
        #数据对应
        url = case_data.get("URL")
        data = case_data.get("data")
        expect_data = case_data.get("expect_data")

        requested = requests.post(url=url, data=json.loads(data))
        log_case_info("test_login_wrong", url, data, expect_data, requested.text)
        self.assertEqual(requested.text, expect_data)  #断言


if __name__ == '__main__':
    unittest.main(verbosity=2)
















