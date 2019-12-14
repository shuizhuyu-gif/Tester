# -*- coding: UTF-8 -*-
#-*-coding:GBK -*-
import unittest
from Objectd.Tester.tools.HTMLTestRunner import HTMLTestRunner
from Objectd.Tester.config.config import *


logging.info("================================== 接口测试开始 ==================================")
print("================================== 接口测试开始 ==================================")
# suite = unittest.defaultTestLoader.discover(test_path)
suite = unittest.defaultTestLoader.discover(test_path)
print("===================================正在读取数据中=================================")
with open(report_file, 'wb') as f:  # 从配置文件中读取

    HTMLTestRunner(stream=f, title="接口测试用例报告", description="测试整体描述", tester="水煮鱼").run(suite)

logging.info("================================== 接口测试结束 ==================================")

print("================================== 接口测试结束 ==================================")
