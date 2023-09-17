from pprint import pprint
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from datetime import datetime


def remove_stock():
    data = pd.read_csv(r"D:\Users\Desktop\New\STRA‘\g_data\stock_classify.csv", index_col=0)
    name = list(data['name'])
    name_remove = [n for i, n in enumerate(name) if n not in name[:i]]
    name_remove = [n for n in name_remove if ('ST' not in n) and ('退' not in n) and (('B') not in n)]
    return name_remove, data


def match_htsc_code():
    stock_name, data = remove_stock()
    sn_array = np.array(stock_name)
    htsc_code = list(
        data[data['name'].isin(sn_array)].drop_duplicates(subset=['htsc_code'], ignore_index=True)['htsc_code'])
    return htsc_code


def remove_long_day_noupdate(engine):
    """
    remove the table that long days no update from the database
    """

    with engine.connect() as conn:
        result = conn.execute(text('show tables')).fetchall()
        all_stock = [n[0] for n in result]

        for stock in all_stock:
            result = \
                conn.execute(text('SELECT * FROM `{}`  ORDER BY `time` DESC LIMIT 1'.format(stock))).fetchall()[
                    0]
            name = result[-1]
            date = datetime.date(result[0])
            today = datetime.date(datetime.now())
            days = (today - date).days
            # print(days)


            if days > 185:
                print(name, date)
                print(conn.execute(text('drop table `{}`'.format(name))))


if __name__ == '__main__':
    # data = match_htsc_code()
    # print(data.index('300256.SZ'))
    # print(len(data))
    engine = create_engine("mysql+pymysql://root:2542415@127.0.0.1:3306/daily_kline_test", echo=False)
    remove_long_day_noupdate(engine)
