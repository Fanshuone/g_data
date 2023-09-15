import pandas as pd
from insight_python.com.insight import common
from insight_python.com.insight.query import *
from insight_python.com.insight.market_service import market_service
from no_ptintf_test import no_printf


@no_printf
def login():
    markets = market_service()

    user = "MDIL1_00275"
    password = "vG_+VN.UYfkSx"
    common.login(markets, user, password)


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    login()
    data = pd.read_csv("申万三级分类.csv", encoding='gbk', delimiter=',', header=[0, 1])
    # print(data.columns)
    industry_code = list(data['l3_code', '(三级行业代码)'])
    industry_name = list(data['l3_name', '(三级行业名称)'])

    # 获取申万行业代码490000下的所有股票基础信息
    # result = get_industry_stocks(industry_code=str(industry_code[0]), classified='sw')[
    #     ['htsc_code', 'name', 'exchange', 'l3_code', 'l3_name']]
    # result1 = get_industry_stocks(industry_code=str(industry_code[1]), classified='sw')[
    #     ['htsc_code', 'name', 'exchange', 'l3_code', 'l3_name']]
    # print(result)
    # print(result1)

    # print(pd.concat([result, result1]))
    result = pd.DataFrame()
    for code in industry_code:
        try:
            singal_data = get_industry_stocks(industry_code=str(code), classified='sw')[['htsc_code', 'name', 'exchange', 'l3_code', 'l3_name']]
            result = pd.concat([result,singal_data],ignore_index=True)
        except Exception as error:
            print(code,error)
    result.to_csv("stock_classify.csv")

