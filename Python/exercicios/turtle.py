import turtle

def quadrado(lado):
    """
    Desenha um quadrado de lado = lado
    """
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    

if __name__ == "_main_":
    meu_lado = 50
    quadrado(meu_lado)


from tkinter import * # importa o módulo
from tkinter.messagebox import *

raiz = Tk() # cria a janela principal
raiz.title("messagebox")

quadro = Frame(raiz)
quadro.pack()

conta = IntVar()
conta.set(0)

mensagem = "Impossivel decrementar!"

def contador(valor):
    conta.set(valor)

etiqueta = Label(quadro, textvariable=conta)
etiqueta.pack()

botao_inc = Button(quadro, text="Incrementa", comand=(lambda : contador(conta.get() + 1)))
botao_inc.pack(side=LEFT)

botao_dec = Button(quadro, text="Decrementa", comand=(lambda : contador(conta.get() - 1) if (conta.get() > 0) else showerror("Decrementa", mensagem)))
botao_dec.pack(side=LEFT)

botao_limpa = Button(quadro, text="Limpa", comand=(lambda : contador(0)))
botao_limpa.pack(side=LEFT)

raiz.mainloop() # chama o ciclo de gestao de eventos




