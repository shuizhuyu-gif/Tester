
import pymysql
import sys
sys.path.append("..")
from Objectd.Tester.config.config import *


#利用插件pymsql与数据库建立连接
def connect_db():
    connect = pymysql.connect(host = db_host,
                              port = db_port,
                              user = db_user,
                              password = db_password,
                              dbname = db_name,
                              charset ="utf8"
    )
    return connect


#数据操作函数

def select_db(sql):
    logging.debug(sql)
    connect = connect_db()   #建立sql连接
    cur = connect.cursor()   #建立游标
    cur.execute(sql)     #执行sql语句
    connect.commit()
    result = cur.fetchall()   #获取sql查询结果
    logging.debug(result)
    cur.close()     #关闭游标
    connect.close()    #关闭sql连接
    #返回sql查询结果
    return result

#设置其他数据库操作函数,注释同上
def other_db(sql):
    logging.debug(sql)
    connect = connect_db()
    cur = connect.cursor()
    try:
        cur.execute(sql)
        connect.commit()
    except Exception as e:
        connect.rollback()   #回滚操作
        logging.error(str(e))   #日志里输出错误
    finally:
        cur.close()
        connect.close()




#sql增删改查函数封装

def select_table(name): #()进行字段设置
    sql = "select * from user where name  ='{}'".format(name)            #sql语句书写可根据类容和需求自行进行优化
    result = select_table(sql)
    return True  if result else False


def insert_table(name,password):
    sql = "insert into user(name,password) values('{}','{}')".format(name,password)       #sql语句书写方式不多赘述
    insert_table(sql)


def delete_table(name):
    sql = "delete from user where name='{}'".format(name)
    delete_table(sql)














