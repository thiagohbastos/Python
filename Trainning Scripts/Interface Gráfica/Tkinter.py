from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from tkinter import *

def teste():
    a = 5+8
    texto_dinamico['text'] = f'Resultado: {a}'

janela = Tk()

janela.title('Teste')
janela.geometry('400x150')

texto_orientacao = Label(janela, text='Texto de teste')
texto_orientacao.grid(column=0, row=0, padx=100, pady=10)

botao = Button(janela, text='Botão teste', command=teste)
botao.grid(column=0, row=1, padx=100, pady=10)

texto_dinamico = Label(janela, text='')
texto_dinamico.grid(column=0, row=2, padx=100, pady=10)

janela.mainloop()
