from stock_remove_demo import remove_stock
from threading import Thread
from insight_python.com.insight import common
from insight_python.com.insight.query import *
from insight_python.com.insight.market_service import market_service
from datetime import datetime

stock_name = remove_stock()


class Multi_Thread_Tomysql(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        pass


if __name__ == '__main__':
    pass