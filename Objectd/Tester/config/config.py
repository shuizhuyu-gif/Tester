
import logging
import os

#项目所属的路径
#在当前文件的上一级目录
master_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#数据目录
data_path = os.path.join(master_path,"data")
#测试用例目录
test_path = os.path.join(master_path,"test")

#更改到log
log_file = os.path.join(master_path,"log","log.txt")
#更改到report文件
report_file = os.path.join(master_path,"report","report.html")

# CRITICAL：致命错误
# ERROR：严重错误
# WARNING：需要给出的提示
# INFO：一般的日志信息
# DEBUG：在debug过程中的debug信息
#对log日志进行配置
logging.basicConfig(level=logging.INFO,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式



# 数据库配置
db_host = "127.0.0.1",
db_port =3306,
db_user ="root",
db_password =123456,
db_name = "wygl"























