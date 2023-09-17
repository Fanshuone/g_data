from pprint import pprint
import numpy as np
import pandas as pd


def remove_stock():
    data = pd.read_csv(r"D:\Users\Desktop\New\STRA‘\g_data\stock_classify.csv", index_col=0)
    name = list(data['name'])
    name_remove = [n for i, n in enumerate(name) if n not in name[:i]]
    name_remove = [n for n in name_remove if ('ST' not in n) and ('退' not in n) and (('B') not in n)]
    return name_remove, data


def match_htsc_code():
    stock_name, data = remove_stock()
    sn_array = np.array(stock_name)
    htsc_code = list(data[data['name'].isin(sn_array)].drop_duplicates(subset=['htsc_code'],ignore_index=True)['htsc_code'])
    return htsc_code


if __name__ == '__main__':
    data = match_htsc_code()
    print(len(data))
