from insight_python.com.insight import common
from insight_python.com.insight.query import *
from insight_python.com.insight.market_service import market_service
from sqlalchemy import create_engine, text
from no_ptintf_test import no_printf


@no_printf
def login():
    markets = market_service()

    user = "MDIL1_00275"
    password = "vG_+VN.UYfkSx"
    common.login(markets, user, password)


login()

time_start_date = "2018-1-1 0:0:0"
time_end_date = "2023-9-12 1:0:0"
time_start_date = datetime.strptime(time_start_date, '%Y-%m-%d %H:%M:%S')
time_end_date = datetime.strptime(time_end_date, '%Y-%m-%d %H:%M:%S')

key = ['300256.SZ', '301329.SZ', '301383.SZ', '301486.SZ',
       '001314.SZ', '603296.SH', '688035.SH', '301319.SZ',
       '688371.SH', '688150.SH','688359.SH', '688550.SH',
       '603931.SH', '688106.SH', '688268.SH' ]
result = get_kline(htsc_code=key,
                   time=[time_start_date, time_end_date],
                   frequency="daily", fq="none")

for i in key:

    print(result[result['htsc_code'].isin([i])])
