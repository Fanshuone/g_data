class Kline_Single():
    def __init__(self, kline):
        self.kline = kline
        if self.kline.empty:
            pass
        else:
            self.name = self.kline['htsc_code'][0]
            self.kline['openinterest'] = 0
            self.kline = self.kline[
                ['time', 'open', 'high', 'low', 'close', 'volume', 'value', 'num_trades', 'openinterest', 'frequency',
                 'htsc_code']]
        # print(self.kline)


class Kline_Multi():
    def __init__(self, multi_kline, stock_code):
        self.multi_kline = multi_kline
        self.stock_code = stock_code
