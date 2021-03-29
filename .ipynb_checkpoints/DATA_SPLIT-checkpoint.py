import pandas as pd
import numpy as np

data = pd.read_csv('14INV457DB.csv', sep=';')
data.head()
data.info()

# ITA 7
ITA_7 = data.query('ita <= 7')
ITA_7.info()
pd.to_pickle(ITA_7, "ITA_7.pkl")

# ITA 8
ITA_8 = data.query('ita <= 8')
ITA_8.info()
pd.to_pickle(ITA_8, "ITA_8.pkl")
