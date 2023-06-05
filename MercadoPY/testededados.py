from chave import link
import requests
import pandas as pd
from IPython.display import display, HTML
from io import StringIO
from tkinter import *

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
    
    texto_cotacoes["text"] = texto

tela = Tk()

tela.title("COTAÇÃO ATUAL")

texto_cotacoes = Label(tela, text="TELA DE COTAÇÕES")
texto_cotacoes.grid(column=0, row=0)

botao = Button(tela, text="COTAÇÕES", command=cotacoes)
botao.grid(column=0, row=1)

texto_cotacoes = Label(tela, text="")
texto_cotacoes.grid(column=0, row=2)


tela.mainloop()