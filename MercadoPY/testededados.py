from chave import link
import requests
import pandas as pd
from IPython.display import display, HTML
from io import StringIO


def cotacoes():
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