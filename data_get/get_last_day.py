from sqlalchemy import text


class Last_Day():
    def __init__(self, engine, all_stock):
        self.engine = engine
        self.all_stock = all_stock

    def g_last_day(self):
        with self.engine.connect() as conn:
            for stock in self.all_stock:
                result = \
                conn.execute(text('SELECT * FROM `{}`  ORDER BY `time` DESC LIMIT 1'.format(stock))).fetchall()[0]
                print(result[0].strftime("%Y-%m-%d"))
                # print(result)


if __name__ == '__main__':
    from sqlalchemy import create_engine

    engine = create_engine("mysql+pymysql://root:2542415@127.0.0.1:3306/data_kline_test1", echo=False)
    from stock_remove import match_htsc_code

    stock_code = match_htsc_code()[5100:]
    ld = Last_Day(engine, stock_code)
    ld.g_last_day()
