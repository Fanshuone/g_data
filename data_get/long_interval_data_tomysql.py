import time
import warnings
from stock_remove import match_htsc_code
from threads_conduct import Separate, Multi_Thread_Tomysql
from login import login
import pandas as pd
from g_kline import G_kline
from sqlalchemy import create_engine, text
from queue import Queue

warnings.filterwarnings("ignore", category=UserWarning)
pd.set_option("display.max_columns", 20)


def long_day_to_insert():
    htsc_code = match_htsc_code()[5100:]
    engine = create_engine("mysql+pymysql://root:2542415@127.0.0.1:3306/data_kline_test1", echo=False)
    queue1 = Queue()
    queue2 = Queue()
    login()
    se = Separate(queue1, queue2)
    mu1 = Multi_Thread_Tomysql(queue2, engine,"replace")
    mu2 = Multi_Thread_Tomysql(queue2, engine,"replace")
    se.start()
    mu1.start()
    mu2.start()
    g_data = G_kline(htsc_code, "2018-1-1 0:0:0", "2023-9-13 23:0:0", frequency='daily', queue1=queue1)
    g_data.start_g()
    se.join()
    mu1.join()
    mu2.join()


if __name__ == '__main__':
    start = time.time()
    long_day_to_insert()
    end = time.time()
    print("消耗时间", round(end - start, 2))
