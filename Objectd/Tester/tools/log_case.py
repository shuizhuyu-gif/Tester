# -*- coding: UTF-8 -*-
#-*-coding:GBK -*-
import json
import sys
sys.path.append("..")
from Objectd.Tester.config.config import *


#设置用例日志输出

def log_case_info(case_name,URL,data,expect_data,response_data):
    #如果入参为字典类型则转换为字符串类型
    if isinstance(data,dict):
        data = json.dumps(data,ensure_ascii=False) #转换格式
    # logging.info("-------------接口测试开始---------------")
    logging.info("测试用例名称：{}".format(case_name))
    logging.info("URL:{}".format(URL))
    logging.info("请求参数：{}".format(data))
    logging.info("预期结果:{}".format(expect_data))
    logging.info("实际结果:{}".format(response_data))
    # logging.info("-------------接口测试结束---------------")
