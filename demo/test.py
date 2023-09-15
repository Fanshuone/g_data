from datetime import datetime
from data_get.login import login
from insight_python.com.insight.query import *
pd.set_option('display.max_columns', 200)
time_start_date = "2023-8-11 0:0:0"
time_end_date = "2023-9-12 10:0:0"
time_start_date = datetime.strptime(time_start_date, '%Y-%m-%d %H:%M:%S')
time_end_date = datetime.strptime(time_end_date, '%Y-%m-%d %H:%M:%S')

# time_start_date = "2021-01-14"
# time_end_date = "2022-10-20"
# time_start_date = datetime.strptime(time_start_date, '%Y-%m-%d')
# time_end_date = datetime.strptime(time_end_date, '%Y-%m-%d')
# 获取510050.SH和601688.SH在指定时间范围内的日K线数据

if __name__ == '__main__':
    login()
    result = get_kline(htsc_code=["000666.SZ"], time=[time_start_date, time_end_date],
                       frequency="daily", fq="none")

    print(result)