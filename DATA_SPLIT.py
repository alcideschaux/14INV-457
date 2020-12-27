import pandas as pd
import numpy as np

data = pd.read_excel('14INV457DB.xlsx', engine='openpyxl')
data.head()
data.info()

ITA_7 = data.query('ita <= 7')
ITA_7.info()

pd.to_pickle(ITA_7, "ITA_7.pkl")
