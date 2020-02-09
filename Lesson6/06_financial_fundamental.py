# pip install simfin
# https://simfin.com/

import pandas as pd
import simfin as sf
import matplotlib.pyplot as plt
from simfin.names import TICKER, REPORT_DATE, PUBLISH_DATE, REVENUE

sf.set_api_key(api_key='free')
sf.set_data_dir('~/simfin_data/')

df1 = sf.load(dataset='income', variant='annual', market='us', 
              index=[TICKER, REPORT_DATE],
              parse_dates=[REPORT_DATE, PUBLISH_DATE])

msft =df1.loc['MSFT']
print(msft.head())
print(";".join((*msft,)))

msft[REVENUE].plot(grid=True)
plt.show(block=True)
