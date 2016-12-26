# coding:utf-8

import MySQLdb
import spider



conn = MySQLdb.connect(host="localhost", user="root", passwd="admin", db="spider_py", charset="utf8")
conn.autocommit(True)
cursor = conn.cursor()
spider.blog(conn)
# 插入获取的数据
# sql = 'insert into artciles(link, name, brief) value(%s, %s, %s)'




