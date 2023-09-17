import time

from sqlalchemy import text, exc
from queue import Queue
from threading import Thread
from finish_queue import finish_queue


class Get_Last_Day(Thread):
    def __init__(self, engine, queue):
        super().__init__()
        self.engine = engine
        self.all_stock = None
        self.queue = queue

    def run(self):
        self.g_table()
        with self.engine.connect() as conn:
            for stock in self.all_stock:
                # try:

                result = \
                    conn.execute(text('SELECT * FROM `{}`  ORDER BY `time` DESC LIMIT 1'.format(stock))).fetchall()[
                        0]
                date = result[0].strftime("%Y-%m-%d")
                name = result[-1]
                self.queue.put((name, date))
                # except exc.ProgrammingError as e:
                #     print(e)
                #     pass
                # print(result)

    def g_table(self):
        with self.engine.connect() as conn:
            result = conn.execute(text('show tables')).fetchall()
            self.all_stock = [n[0] for n in result]


class Align_Time(Thread):
    def __init__(self, queue1, queue2):
        super().__init__()
        self.queue1 = queue1
        self.queue2 = queue2

    @finish_queue
    def run(self):
        code_time = self.queue1.get(timeout=5)
        code_time_list = [code_time]
        i = 1
        while True:
            code_time = self.queue1.get(timeout=5)

            if code_time_list[0][1] == code_time[1] and len(code_time_list) <= 50:

                code_time_list.append(code_time)
                i += 1

            else:
                i += 1
                self.queue2.put(code_time_list)
                code_time_list = [code_time]

            if i == 5156:
                self.queue2.put(code_time_list)


if __name__ == '__main__':
    start = time.time()
    from sqlalchemy import create_engine

    engine = create_engine("mysql+pymysql://root:2542415@127.0.0.1:3306/daily_kline_test", echo=False)
    code_queue = Queue()
    align_list = Queue()
    gld = Get_Last_Day(engine, code_queue)
    at = Align_Time(code_queue, align_list)
    gld.start()
    at.start()
    while 1:
        print(align_list.get(timeout=15))
    gld.join()
    at.join()

    end = time.time()
    print(start - end)
