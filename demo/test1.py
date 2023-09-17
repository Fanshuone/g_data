# from queue import Queue
#
# queue = Queue()
#
# queue.put(1)
# print(queue.get(timeout=20))
# print(queue.get(timeout=20))
# import time
#
# start = time.time()
# time.sleep(3.14)
# end = time.time()
# print("消耗时间",round(end-start,2))
import datetime
from pprint import pprint

from sqlalchemy import create_engine,text

# 创建数据库引擎
engine = create_engine("mysql+pymysql://root:2542415@127.0.0.1:3306/data_kline_test1", echo=False)

# 执行原生 SQL 查询
result = engine.connect().execute(text('SELECT * FROM `603279.sh`  ORDER BY `time` DESC LIMIT 1'))

# 获取查询结果
last_row = result.fetchall()[0]

# 打印最后一条数据
pprint(last_row[0].strftime("%Y-%m-%d"))


a = [1,2]
print(a[0:11])

from datetime import datetime

print(datetime.now().strftime('%Y-%m-%d'))
print(type(datetime.now()))
print(datetime.date(datetime.now()))

past = datetime.date(datetime.strptime("2021-11-11", '%Y-%m-%d'))

today = datetime.date(datetime.now())

print((today-past).days)
print(type((today-past).days))

print(3^2)

import numpy as np
a = np.array([1,2,3])
print(a**2)
print(len(a))
print(str(a))
print(np.e**a)
print(np.log(5))

b = np.array([[1, 2],
              [1,2]])
c = np.array([[1, 2]])
# print(b@c)
print(c@b)
print(b[:,1])
print(b.tolist())
print(b**2)
print(b[:,1])


d = [[1],[2]]
print(c @ d)
print(c@c.transpose())
print(c.transpose())

print(datetime.strptime('2023-09-13' + ' 0:0:0', '%Y-%m-%d %H:%M:%S'))
print(datetime.strptime(datetime.now().strftime('%Y-%m-%d')+ ' 23:0:0','%Y-%m-%d %H:%M:%S'))