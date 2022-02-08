from tkinter import *
from tkinter import ttk, filedialog, END
from ttkbootstrap import Style, Meter
from ttkbootstrap.constants import *

class Funcoes():
    def iniciar_testes(self):
        self.box_salvar.configure(state='disable')
        self.box_squad.configure(state='disable')
        self.bt_iniciar.configure(state='normal', text='Testes iniciados!', bootstyle=WARNING, command=None)
        try:
            self.txt_destino_arquivo.configure(state='disable')
        except AttributeError:
            pass
        self.root.geometry('450x750')
        self.frame_um.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.35)
        self.frame_2()
        self.frame_3()

class Janela_principal(Funcoes):
    def __init__(self):
        #Atributos
        self.estilo_1 = Style(theme='cosmo')
        #ttk.Style().configure('TEntry')
        ttk.Style().configure('TButton', font='sans-serif 10')
        #Define tema e cria o objeto janela
        self.root = self.estilo_1.master
        #Funções
        self.janela()
        self.frame_1()
        self.titulo()
        self.campos()
        self.botoes()
        #Mantendo janela aberta
        self.root.mainloop()

    def janela(self):
        self.root.title('BOT de Teste de Fluxo ISPs Automatizado')
        self.larg_janela = 450
        self.compr_janela = 277
        self.root.geometry(f'{self.larg_janela}x{self.compr_janela}')
        self.root.resizable(False, False)
        self.root.config(background='#257DFE')

    def frame_1(self):
        self.frame_um = Frame(self.root)
        self.frame_um.place(relx=0.02, rely=0.027, relwidth=0.96, relheight=0.9461)

    def frame_2(self):
        self.frame_dois = ttk.LabelFrame(self.root, text=' Status ')
        self.frame_dois.place(relx=0.02, rely=0.37, relwidth=0.96, relheight=0.15)

    def frame_3(self):
        self.frame_tres = ttk.LabelFrame(self.root, text=' Observações ')
        self.frame_tres.place(relx=0.02, rely=0.53, relwidth=0.96, relheight=0.46)

    def titulo(self):
        self.titulo_lb = ttk.Label(self.frame_um, text='BOT de Teste de Fluxo LP', font=('sans-serif', '18', 'bold'),
                                   foreground='#257DFE')
        self.titulo_lb.pack(pady=8)

    def campos(self):
        #Campo Squad
        self.lb_squad = ttk.Label(self.frame_um, text='Escolha o Squad:', font=('sans-serif', '13'), foreground='black')
        self.lb_squad.place(relx=0.02, rely=0.265)
            #Combobox
        self.box_squad = ttk.Combobox(
            self.frame_um, values=['Todos os Squads', 'Eva', 'Wall-e', 'Burn-e', 'M-O'], font=('sans-serif', '13'),
            foreground='black', state='readonly', takefocus=False
            )
        self.box_squad.current(0)
        self.box_squad.place(relx=0.35, rely=0.24, relwidth=0.625)

        # Campo "Salvar""
        self.lb_salvar = ttk.Label(self.frame_um, text='Deseja Salvar o resultado?', font=('sans-serif', '13'), foreground='black')
        self.lb_salvar.place(relx=0.02, rely=0.45)
            # Combobox
        self.box_salvar = ttk.Combobox(
            self.frame_um, values=['Sim', 'Não'], font=('sans-serif', '13'), foreground='black', state='readonly', takefocus=False
        )
        self.box_salvar.current(1)
        self.box_salvar.place(relx=0.50, rely=0.425, relwidth=0.475)
        self.box_salvar.bind('<<ComboboxSelected>>', self.reacao_box_salvar)

    def botoes(self):
        self.bt_iniciar = ttk.Button(self.frame_um, text='Iniciar Testes', width=20, command=self.iniciar_testes)
        self.bt_iniciar.pack(pady=(162, 0))

    def reacao_box_salvar(self, evento=None):
        if self.box_salvar.get() == "Sim":
            self.lb_destino_arquivo = ttk.Label(self.frame_um, text='Destino do arquivo: ', font=('sans-serif', '13'),
                                                foreground='black')
            self.lb_destino_arquivo.place(relx=0.02, rely=0.625)
            #Campo de destino do arquivo
            self.txt_destino_arquivo = Entry(self.frame_um, font=('sans-serif', 9), fg='gray', state='normal')
            self.txt_destino_arquivo.place(relx=0.375, rely=0.615, relwidth=0.60, relheight=0.12)
            self.txt_destino_arquivo.insert('1', r'S:\Inovação\Planejamento\3 - MIS\Gerencial\Acompanhamento das ISPS - Semanal\Testes de Fluxo')

        else:
            try:
                self.lb_destino_arquivo.destroy()
                self.txt_destino_arquivo.destroy()
            except:
                pass

Janela_principal()

