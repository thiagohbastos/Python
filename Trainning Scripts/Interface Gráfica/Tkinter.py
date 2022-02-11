from tkinter import *
from tkinter import ttk, filedialog, END
from ttkbootstrap import Style
#from PIL import Image, ImageTk
#from urllib.request import urlopen
#from io import BytesIO

style = Style(theme='cosmo')
root = style.master

class Funcoes():
    def caminho_arquivos(self):
        teste = filedialog.askopenfilenames()
        return teste
    def limpa_tela(self):
        self.entry_teste.delete(0, END)
        self.texto.delete('1.0', END)

class Application(Funcoes):
    # Função inicializada com a classe
    def __init__(self):
        # Atributo janela recebe a variável janela do módulo Tk
        self.root = root
        self.cor_1 = '#00587C' #Azul Bem Escuro
        self.cor_2 = '#2897B2' #Azul pouco mais claro
        self.cor_3 = '#EBF8FB' #Azul claro
        # Chamando as funções da classe
        self.tela()
        self.frames_gerais()
        self.frame_de_lista()
        self.imagens()
        self.criando_widgets()
        self.frame_de_lista()
        self.teste()
        # Mantendo a janela ativa
        self.root.mainloop()
    """*** LEGENDA ***
    bg = background
    bd = borderwidth
    fg = cor da fonte
    font = nome, tamanho e tipo da fonte (bold, italic, etc)
    """

    def tela(self):
        self.root.title('Teste')
        self.root.configure(background=self.cor_1)
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    def frames_gerais(self):
        self.frame_geral = Frame(self.root, bd=4, background=self.cor_3, highlightbackground=self.cor_2, highlightthickness=2)
        self.frame_geral.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
    def frame_de_lista(self):
        #Criando o frame com o nome das colunas
        self.lista_generica = ttk.Treeview(self.frame_geral, height=3, columns=('col1', 'col2', 'col3'))
        #Cabeçalho das colunas
        self.lista_generica.heading('#0', text='')
        self.lista_generica.heading('#1', text='Teste1')
        self.lista_generica.heading('#2', text='Teste2')
        self.lista_generica.heading('#3', text='Teste3')
        #Tamanho das colunas
        self.lista_generica.column('#0', width=1)
        self.lista_generica.column('#1', width=100)
        self.lista_generica.column('#2', width=200)
        self.lista_generica.column('#3', width=200)
        #Posição da lista
        self.lista_generica.place(relx=0.01, rely=0.5, relwidth=0.8, relheight=0.4)
        #Barra de Rolagem
        self.scroll_vertical = Scrollbar(self.frame_geral, orient='vertical')
        self.scroll_vertical.place(relx=0.81, rely=0.5, relwidth=0.05, relheight=0.4)
        #Linkando a barra de rolagem e a lista
        self.lista_generica.configure(yscrollcommand=self.scroll_vertical)
    def imagens(self):
        pass
        #self.imagem = PhotoImage(file=r"C:\Users\thiago.bastos\Desktop\Temporários\No meu container, roda.png")
        #self.imagem = self.imagem.subsample(5, 5)
        #self.label_imagem = Label(self.frame_geral, image=self.imagem)
        #self.label_imagem.place(relx=0.9, rely=0.9, relheight=0.1, relwidth=0.1)
        # Imagem de URL
        #self.URL = "http://www.universeofsymbolism.com/images/ram-spirit-animal.jpg"
        #u = urlopen(self.URL)
        #raw_data = u.read()
        #u.close()
        #im = Image.open(BytesIO(raw_data))
        #photo = ImageTk.PhotoImage(im)
        #self.label_imagem = tk.Label(self.frame_1, image=photo)
        #self.label_imagem.image = photo
        #self.label_imagem.pack()'''
    def criando_widgets(self):
            #WIDGET Limpar
        # Descrição do campo "Teste"
        self.lb_teste = Label(self.frame_geral, text='Input de Teste abaixo:', bg=self.cor_3,
                                 font=('calibri', 12), fg=self.cor_1)
        self.lb_teste.place(relx=0.01, rely=0, relheight=0.08)
        # Espaço para input do Campo "Teste"
        self.entry_teste = Entry(self.frame_geral, bg='white', font=('calibri', 12))
        self.entry_teste.place(relx=0.01, rely=0.065, relwidth=0.23, relheight=0.05)
        # Objeto e localização do Botão "Limpar"
        self.bt_teste = Button(self.frame_geral, text='Limpar', fg='white', bg=self.cor_2,
                                  bd=2, font=('calibri', 12, 'bold'), command=self.limpa_tela)
        self.bt_teste.place(relx=0.25, rely=0.065, relwidth=0.1, relheight=0.05)
    def teste(self):
        self.texto = Text(self.frame_geral)
        self.texto.place(relx=0.01, rely=0.12, relwidth=0.8, relheight=0.35)

Application()