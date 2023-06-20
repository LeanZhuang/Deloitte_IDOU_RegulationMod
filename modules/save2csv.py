import pandas as pd
from datetime import datetime
date = datetime.now().strftime("%y%m%d")

path = '/Users/zhuangyuhao/VSCodeProjects/RegMod/'


def save2csv(df, name):
    df.to_csv(path + 'outputs/' + name + '_' + date + '.csv', index=False, encoding='utf_8')