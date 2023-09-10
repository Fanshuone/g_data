from pprint import pprint

import pandas as pd


def remove_stock():
    data = pd.read_csv("stock_classify.csv", index_col=0)
    name = list(data['name'])
    name_remove = [n for i, n in enumerate(name) if n not in name[:i]]
    name_remove = [n for n in name_remove if ('ST' not in n) and ('退' not in n) and (('B') not in n)]
    return name_remove


if __name__ == '__main__':
    name_remove = remove_stock()
    print(len(name_remove))

    pprint(name_remove)
