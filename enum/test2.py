# def get_point():
#     len=0
#     def get_sum(num):
#         nonlocal len
#         len+=num
#         return len
#     return get_sum
#
# f=get_point()
# print(f(1))
# print(f.__closure__[0].cell_contents)
# print(f(5))
# print(f.__closure__[0].cell_contents)
# print(f(5))
# print(f.__closure__[0].cell_contents)


# len=0
# def get_point(num):
#     global len
#     len+=num
#     return len
# print(get_point(1))
# print(get_point(2))

# f=lambda x,y:x+y
# print(f(1,2))


# l=[2,2,3,4]
# l1=[1,3,2,7]
# f=lambda x,y:x if x>y else y
# l2=map(f,l,l1)
# print(list(l2))

# from functools import reduce
# l=[(1,1),(2,4),(3,-1)]
# # ans=reduce(lambda (x1,y1),(x2,y2):(x1+x2,y1+y2),l,(0,0))
# ans=reduce(lambda x,y:(x[0]+y[0],x[1]+y[1]),l,(0,0))
# print(ans)

import time

'''装饰器'''
# def decorator(func):
#     def add(*var,**kw):
#         func(*var,**kw)
#         print('****************')
#     return add
#
# @decorator
# def f():
#     pass
#
# @decorator
# def f1():
#     print('First:')
#
#
# @decorator
# def f2(num1, num2):
#     print(num1, 'VS', num2)
#
#
# @decorator
# def f3(num1, num2, **num3):
#     print(num1, 'VS', num2)
#     print(num3)
#
#
# if __name__ == '__main__':
#     f()
#     f1()
#     f2('1号', '5号')
#     f3('22号', '7号', a=1, b=2, c=3)


# a=[1,2,3,4,5,6]
# b=[i if i<=3 else i**2 for i in a]
# c=[i**2 for i in a if i<=3]
# print(b)
# print(c)


# import pymysql
#
# # 打开数据库连接,参数1:主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名称
# db = pymysql.connect("localhost", "root", "ltlmhlq1998", "mrsoft")
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print ("Database version : %s " % data)
# # 关闭数据库连接
# db.close()

# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "ltlmhlq1998", "mrsoft")
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS books")
# # 使用预处理语句创建表
# sql = """
# CREATE TABLE books (
#   id int(8) NOT NULL AUTO_INCREMENT,
#   name varchar(50) NOT NULL,
#   category varchar(50) NOT NULL,
#   price decimal(10,2) DEFAULT NULL,
#   publish_time date DEFAULT NULL,
#   PRIMARY KEY (id)
# ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
# """
# # 执行SQL语句
# cursor.execute(sql)
# # 关闭数据库连接
# db.close()

# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "ltlmhlq1998", "mrsoft",charset="utf8")
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
# # 数据列表
# data = [("零基础学Python",'Python','79.80','2018-5-20'),
#         ("Python从入门到精通",'Python','69.80','2018-6-18'),
#         ("零基础学PHP",'PHP','69.80','2017-5-23'),
#         ("PHP项目开发实战入门",'PHP','79.80','2016-5-23'),
#         ("零基础学Java",'Java','69.80','2017-5-23'),
#         ]
# try:
#     # 执行sql语句，插入多条数据
#     cursor.executemany("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)", data)
#     # 提交数据
#     db.commit()
# except:
#     # 发生错误时回滚
#     db.rollback()
#
# # 关闭数据库连接
# db.close()


# class Alice:
#     name="BBB"
#
# Ali=Alice()
# print(Ali.name)
# Alice.name='CCC'
# print(Alice.name)
# b=Alice()
# print(b.name)

# from multiprocessing import Process
#
#
# def test(interval):
#     print('我是子进程')
#
#
# def main():
#     print('主进程开始')
#     p = Process(target=test, args=(1,))
#     p1 = Process(target=test, args=(2,))
#     p.start()
#     p1.start()
#     # time.sleep(0.1)
#     print('主进程结束')
#
#
# if __name__ == '__main__':
#     main()


a=int(input())
b=int(input())

print(a+b)