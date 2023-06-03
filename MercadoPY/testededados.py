from chave import chave_api
import requests
import pandas as pd
from IPython.display import display, HTML
from io import StringIO

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

def cotaces():
    req = requests.get(link)
    
    req_dic = req.json()

    dolar = req_dic['USDBRL']['bid']
    euro = req_dic['EURBRL']['bid']
    bitcoin = req_dic['BTCBRL']['bid']

    texto = f'''
    dolar: {dolar}
    euro: {euro}
    bitcoin: {bitcoin}'''

    print(texto)

cotaces()