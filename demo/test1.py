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
