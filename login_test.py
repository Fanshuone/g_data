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

time_start_date = "2021-05-14 15:10:11"
time_end_date = "2021-05-18 11:20:50"
time_start_date = datetime.strptime(time_start_date, '%Y-%m-%d %H:%M:%S')
time_end_date = datetime.strptime(time_end_date, '%Y-%m-%d %H:%M:%S')

result = get_kline(htsc_code=["510050.SH", "601688.SH"], time=[time_start_date, time_end_date],
                   frequency="daily", fq="none")

print(result)
