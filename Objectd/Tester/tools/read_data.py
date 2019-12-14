# -*- coding: UTF-8 -*-
#-*-coding:GBK -*-

import xlrd

def excel_data_list(data_file,sheet):
    data_list =[]    #空列表装数据
    open = xlrd.open_workbook(data_file)  #打开test_data
    obtain = open.sheet_by_name(sheet)  #获取excel工作簿
    header = obtain.row_values(0)     #获取标题行数据
    for i in range(1,obtain.nrows):     #跳过标题行，直接从第二行取数据
        dt = dict(zip(header,obtain.row_values(i)))     #组装为字典
        data_list.append(dt)
    return data_list


def get_test_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data["case_name"]:      #对参数与标题进行去重
            return case_data
        #查询不到数据返回None


if __name__ == '__main__':
    data_list = excel_data_list("test_data.xlsx","login")       #读取Excel的数据,工作簿名login的所有数据
    case_data = get_test_data(data_list,"test_login_normal")      #查找case_name 为test_login_normal 的所有用例数据
    print(case_data)










