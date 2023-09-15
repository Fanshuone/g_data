from insight_python.com.insight import common
from insight_python.com.insight.market_service import market_service
from no_ptintf_test import no_printf


@no_printf
def login():
    markets = market_service()

    user = "MDIL1_00275"
    password = "vG_+VN.UYfkSx"
    common.login(markets, user, password)


if __name__ == '__main__':
    login()