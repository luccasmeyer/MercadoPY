from tkinter import *
from testededados import cotacoes



tela = Tk()

tela.title("COTAÇÃO ATUAL")

botao = Button(tela, text="COTAÇÕES", command=cotacoes)
botao.grid(column=0, row=1)

texto_cotacoes = Label(tela, text="")
texto_cotacoes.grid(column=0, row=2)

tela.mainloop()