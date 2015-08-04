# coding=utf-8
# python 操作 oracle 数据库

import cx_Oracle
import xdrlib ,sys
import xlrd

def importdata_text(dbstr,tablename,fileinfo,filesplit):
    if dbstr=="tran1" :
        connect=cx_Oracle.connect('tran1','bfbusicrm','132.80.247.18:1521/ywqydb')
    elif dbstr=="ngcrm" :
        connect=cx_Oracle.connect('uop_crm1','ailkcubj','132.80.241.214:11521/ngcrm')
    couttotal = len(open(fileinfo,'rU').readlines())
    instance = open(fileinfo)
    lines =[]
    countpercent=0
    countnow=0
    column=0
    column_str=""
    for line in instance.readlines():
        column=len(line.split(filesplit))
        lines.append(line.split(filesplit))
        countpercent+=1
        countcomp=countpercent*100/couttotal
        if countcomp>countnow :
            tem='%d' %countcomp
            print "load %s%s...." %(tem,'%')
            countnow=countcomp
    instance.close()
    for i in range(0,column):
        column_str+=":%d,"%(i+1)
    column_str = column_str[:-1]
    var = '''insert into %s values(%s)''' % (tablename,column_str)
    cursor = connect.cursor()
    cursor.executemany(var,lines);  
    cursor.close();
    connect.commit();
    connect.close();
    
def importdata_excel(dbstr,tablename,fileinfo):
    if dbstr=="tran1" :
        connect=cx_Oracle.connect('tran1','bfbusicrm','132.80.247.18:1521/ywqydb')
    elif dbstr=="ngcrm" :
        connect=cx_Oracle.connect('uop_crm1','ailkcubj','132.80.241.214:11521/ngcrm')
    data = xlrd.open_workbook(fileinfo)
    table = data.sheets()[0]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    lines =[]
    countpercent=1
    countnow=0
    column_str=""
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        lines.append(row)
        countpercent+=1
        countcomp=countpercent*100/nrows
        if countcomp>countnow :
            tem='%d' %countcomp
            print "load %s%s...." %(tem,'%')
            countnow=countcomp
    for i in range(0,ncols):
        column_str+=":%d,"%(i+1)
    column_str = column_str[:-1]
    var = '''insert into %s values(%s)''' % (tablename,column_str)
    cursor = connect.cursor()
    cursor.executemany(var,lines);  
    cursor.close();
    connect.commit();
    connect.close();

dbstr=raw_input("please input which db want to import?(tran1,ngcrm)")

tablename=raw_input("please input table name:")

fileinfo=raw_input("please input file path and name:")

if fileinfo.split(".")[-1]=="xls" or fileinfo.split(".")[-1]=="xlsx" :
    importdata_excel(dbstr,tablename,fileinfo)
else :
    filesplit=raw_input("please input file split str:")
    importdata_text(dbstr,tablename,fileinfo,filesplit)





