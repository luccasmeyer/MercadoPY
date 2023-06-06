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
tela.geometry("300x300")
tela.title("COTAÇÃO ATUAL")


texto_cotacoes = Label(tela, text="TELA DE COTAÇÕES")
texto_cotacoes.grid(column=0, row=0, padx=75, pady=10)

botao = Button(tela, text="COTAÇÕES DAS MOEDAS", command=cotacoes)
botao.grid(column=0, row=1, padx=75, pady=10)


texto_cotacoes = Label(tela, text="")
texto_cotacoes.grid(column=0, row=2, padx=75, pady=10)


tela.mainloop()

#tentar deixar o label das moedas com o mesmo numero de caracteres
#teste de pull request