import time

from get_last_day import Get_Last_Day, Align_Time
from sqlalchemy import create_engine
from queue import Queue
from login import login
from threads_conduct import Separate, Multi_Thread_Tomysql
from g_kline import G_Short_Kline


def short_day_to_insert():
    login()
    engine = create_engine("mysql+pymysql://root:2542415@127.0.0.1:3306/daily_kline_test", echo=False)
    code_queue = Queue()
    align_list = Queue()
    queue1 = Queue()
    queue2 = Queue()

    get_last_day = Get_Last_Day(engine, code_queue)
    align_time = Align_Time(code_queue, align_list)

    se = Separate(queue1, queue2)
    mu1 = Multi_Thread_Tomysql(queue2, engine, "append")
    mu2 = Multi_Thread_Tomysql(queue2, engine, "append")

    get_last_day.start()
    align_time.start()
    se.start()
    mu1.start()
    mu2.start()

    g_data = G_Short_Kline(align_list, queue1, 'daily')
    g_data.start_g()

    get_last_day.join()
    align_time.join()
    se.join()
    mu1.join()
    mu2.join()


if __name__ == '__main__':
    start = time.time()
    short_day_to_insert()
    end = time.time()
    print("消耗时间", start-end)
