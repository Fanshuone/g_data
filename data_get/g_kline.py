import datetime

from insight_python.com.insight.query import *
from kline_struct import Kline_Single, Kline_Multi
from insight_python.com.insight import common
from finish_queue import finish_queue

class G_Long_kline():
    def __init__(self, all_stock, start, end, frequency, queue1):
        self.stock_code = None
        self.all_stock = all_stock
        self.start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        self.end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        self.frequency = frequency
        self.queue1 = queue1

    def start_g(self):
        print("开始start_g")
        for i in range(0, len(self.all_stock), 10):
            self.stock_code = self.all_stock[i:i + 10]
            k_line = get_kline(htsc_code=self.stock_code, time=[self.start, self.end], frequency=self.frequency,
                               fq='pre')
            self.queue1.put(Kline_Multi(k_line, self.stock_code))
        print("结束start_g")
        common.fini()


class G_Short_Kline():
    def __init__(self, queue1, queue2,frequency):
        self.end = None
        self.start = None
        self.queue1 = queue1
        self.queue2 = queue2
        self.frequency = frequency

    @finish_queue
    def start_g(self):
        while 1:
            code_time_list = self.queue1.get(timeout=5)
            # print(code_time_list)
            code = []
            time = code_time_list[0][1] + ' 23:0:0'
            for p in code_time_list:
                code.append(p[0])
            self.start = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            self.end = datetime.strptime(datetime.now().strftime('%Y-%m-%d')+ ' 23:0:0','%Y-%m-%d %H:%M:%S')
            k_line = get_kline(htsc_code=code, time=[self.start, self.end], frequency=self.frequency,
                               fq='pre')
            self.queue2.put(Kline_Multi(k_line,code))
            # print(k_line)
