# maximum loss I can expect my portfolio to have with a time horizon X and a certainty of Y%?

# Historical Simulation
# Monte Carlo
# Variance-Covariance

import numpy as np
import pandas as pd
from pandas.tseries.offsets import BDay
import datetime

from tiingo import TiingoClient # documentation here: https://pypi.org/project/tiingo/
# alternative: https://www.quandl.com/
import warnings
warnings.filterwarnings('ignore') #ignore tiingo warnings


tcl = TiingoClient({ 'api_key': 'b2ca7ff28f2bdc6952d7e14b7c27d6f84604a62e666f2e' })
#print(tcl.get_ticker_metadata("GOOGL")) # information about the ticker

# get open, close, high, low, volume + adj_x, 
#example_ticker_history = tcl.get_dataframe("GOOGL")
#print(example_ticker_history.head())

# same as before BUT multiple tickers, only one metric_name if multiple tickers
#example_ticker_history = tcl.get_dataframe(['GOOGL', 'AAPL'], frequency='weekly', metric_name='volume', startDate='2020-01-01', endDate='2020-02-29')
#print(example_ticker_history.head(10))



##########################
## lets compute the VaR ##
##########################
portfolio = {
    'TSLA': 5,
    'MSFT': 20,
    'AAPL': 10
}
tickers = portfolio.keys()
scenarios = 500
confidence = 99

endDate = datetime.date.today() - datetime.timedelta(days=1)
startDate = endDate - BDay(500)
print(f"Getting tickers {tickers} from {startDate} to {endDate}")
tickers_history = tcl.get_dataframe(tickers, frequency='daily', metric_name='close', startDate=startDate, endDate=endDate)

# compute portfolio total value
def computeTotalValue(row):
    result = np.zeros((row.shape[0],)) # preallocate
    for key in portfolio:
        np.sum([result, row[key]*portfolio[key]], axis=0,  out=result)
    return result
tickers_history = tickers_history.assign(TotalValue = computeTotalValue)

# change % con giorno prima
tickers_history['Perc_Change'] = tickers_history['TotalValue'].pct_change() 

lastValueDate = tickers_history.index.max()
portfolioFinalTotalValue = tickers_history.loc[lastValueDate]['TotalValue']
print(f"last value: {portfolioFinalTotalValue} (Date: {lastValueDate})")
tickers_history['TotalValue_Change'] = portfolioFinalTotalValue * tickers_history['Perc_Change'] 
print(tickers_history.head(10))

ValueLocForPercentile = round(len(tickers_history) * (1 - (confidence / 100)))
SortedHistData = tickers_history.sort_values(by=['TotalValue_Change'])
var = SortedHistData.iloc[ValueLocForPercentile + 1, len(SortedHistData.columns)-1] # * np.sqrt(VarDaysHorizon)
print(f"The portfolio's VaR is: {round(var,2)}")