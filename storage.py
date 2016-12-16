# coding:utf-8

import MySQLdb
import spider

conn = MySQLdb.connect(host='localhost', user='root', passwd='admin', db='spider_py', charset='utf-8')
conn.autocommit(True)
cursor = conn.cursor()

# 插入获取的数据
sql = 'insert into artciles(title, content, url) value(%s, %s, %s)'
param = spider.
cursor.execute(sql, param)



