import pandas as pd
import numpy as np

data = pd.read_excel('14INV457DB.xlsx')
data.head()
data.info()

# ITA 1
ITA_1 = data.query('ita <= 1')
pd.to_pickle(ITA_1, "ITA_1.pkl")

# ITA 2
ITA_2 = data.query('ita <= 2')
pd.to_pickle(ITA_2, "ITA_2.pkl")

# ITA 3
ITA_3 = data.query('ita <= 3')
pd.to_pickle(ITA_3, "ITA_3.pkl")

# ITA 4
ITA_4 = data.query('ita <= 4')
pd.to_pickle(ITA_4, "ITA_4.pkl")

# ITA 5
ITA_5 = data.query('ita <= 5')
pd.to_pickle(ITA_5, "ITA_5.pkl")

# ITA 6
ITA_6 = data.query('ita <= 6')
pd.to_pickle(ITA_6, "ITA_6.pkl")

# ITA 7
ITA_7 = data.query('ita <= 7')
pd.to_pickle(ITA_7, "ITA_7.pkl")

# ITA 8
ITA_8 = data.query('ita <= 8')
pd.to_pickle(ITA_8, "ITA_8.pkl")

# ITA 9
ITA_9 = data.query('ita <= 9')
pd.to_pickle(ITA_9, "ITA_9.pkl")

# ITA 10
ITA_10 = data.query('ita <= 10')
pd.to_pickle(ITA_10, "ITA_10.pkl")
