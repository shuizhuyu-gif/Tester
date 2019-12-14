
import logging
import os

#��Ŀ������·��
#�ڵ�ǰ�ļ�����һ��Ŀ¼
master_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#����Ŀ¼
data_path = os.path.join(master_path,"data")
#��������Ŀ¼
test_path = os.path.join(master_path,"test")

#���ĵ�log
log_file = os.path.join(master_path,"log","log.txt")
#���ĵ�report�ļ�
report_file = os.path.join(master_path,"report","report.html")

# CRITICAL����������
# ERROR�����ش���
# WARNING����Ҫ��������ʾ
# INFO��һ�����־��Ϣ
# DEBUG����debug�����е�debug��Ϣ
#��log��־��������
logging.basicConfig(level=logging.INFO,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log��ʽ
                    datefmt='%Y-%m-%d %H:%M:%S',  # ���ڸ�ʽ
                    filename=log_file,  # ��־����ļ�
                    filemode='a')  # ׷��ģʽ



# ���ݿ�����
db_host = "127.0.0.1",
db_port =3306,
db_user ="root",
db_password =123456,
db_name = "wygl"























