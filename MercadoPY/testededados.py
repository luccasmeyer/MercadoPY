from chave import chave_api
import requests
import pandas as pd
from IPython.display import display, HTML
from io import StringIO


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey={chave_api}&datatype=csv'
r = requests.get(url)


tabala = pd.read_csv(StringIO(r.text))
display(tabala)