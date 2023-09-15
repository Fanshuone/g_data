from insight_python.com.insight.query import *
from kline_struct import Kline_Single, Kline_Multi
from insight_python.com.insight import common

class G_kline():
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
