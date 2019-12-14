
import pymysql
import sys
sys.path.append("..")
from Objectd.Tester.config.config import *


#���ò��pymsql�����ݿ⽨������
def connect_db():
    connect = pymysql.connect(host = db_host,
                              port = db_port,
                              user = db_user,
                              password = db_password,
                              dbname = db_name,
                              charset ="utf8"
    )
    return connect


#���ݲ�������

def select_db(sql):
    logging.debug(sql)
    connect = connect_db()   #����sql����
    cur = connect.cursor()   #�����α�
    cur.execute(sql)     #ִ��sql���
    connect.commit()
    result = cur.fetchall()   #��ȡsql��ѯ���
    logging.debug(result)
    cur.close()     #�ر��α�
    connect.close()    #�ر�sql����
    #����sql��ѯ���
    return result

#�����������ݿ��������,ע��ͬ��
def other_db(sql):
    logging.debug(sql)
    connect = connect_db()
    cur = connect.cursor()
    try:
        cur.execute(sql)
        connect.commit()
    except Exception as e:
        connect.rollback()   #�ع�����
        logging.error(str(e))   #��־���������
    finally:
        cur.close()
        connect.close()




#sql��ɾ�Ĳ麯����װ

def select_table(name): #()�����ֶ�����
    sql = "select * from user where name  ='{}'".format(name)            #sql�����д�ɸ������ݺ��������н����Ż�
    result = select_table(sql)
    return True  if result else False


def insert_table(name,password):
    sql = "insert into user(name,password) values('{}','{}')".format(name,password)       #sql�����д��ʽ����׸��
    insert_table(sql)


def delete_table(name):
    sql = "delete from user where name='{}'".format(name)
    delete_table(sql)














