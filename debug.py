# coding:utf-8
import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="admin", db="spider_py", charset="utf8")
conn.autocommit(True)
cursor = conn.cursor()

sql = "insert into articles(title, content, url) value(%s, %s, %s)"
param = (u"APICloud 微信授权登录",
         u"官网 API连接",
         'https://my.oschina.net'
         )
n = cursor.execute(sql, param)
# conn.commit()
print (n)

param2 = (u"HTML父页面调用iframe子页面中js变量和方法",
          u'获取子页面dom:$("iframe").eq(0).contents().find("selector") 调用子页面js变量和方法:$("iframe").eq(0)[0].contentWindow.method()',
          u'https://my.oschina.net/watcher/blog/806835')
m = cursor.execute(sql, param2)
print (m)

