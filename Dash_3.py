import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()

df = web.DataReader('TSLA', 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index('Date', inplace=True)
df = df.drop('Symbol', axis=1)
#print(df.head())




