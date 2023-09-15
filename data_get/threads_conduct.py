from threading import Thread
from kline_struct import Kline_Single, Kline_Multi
from finish_queue import finish_queue


class Separate(Thread):
    def __init__(self, queue1, queue2):
        super().__init__()
        self.k_line = None
        self.queue1 = queue1
        self.queue2 = queue2

    @finish_queue
    def run(self):
        while 1:
            self.k_line = self.queue1.get(timeout=15)
            for n in self.k_line.stock_code:
                single_kline = self.k_line.multi_kline[self.k_line.multi_kline['htsc_code'].isin([n])]
                single_kline = single_kline.reset_index(drop=True)
                kline = Kline_Single(single_kline)
                self.queue2.put(kline)


class Multi_Thread_Tomysql(Thread):
    def __init__(self, queue2, engine,pattern):
        super().__init__()
        self.data = None
        self.queue2 = queue2
        self.engine = engine
        self.pattern = pattern

    @finish_queue
    def run(self):
        while 1:
            self.data = self.queue2.get(timeout=15)
            if self.data.kline.empty:
                pass
            else:
                self.data.kline.to_sql(name=self.data.name.lower(), con=self.engine, if_exists=self.pattern, index=False)
            # print(self.data.kline)
