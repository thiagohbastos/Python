from tkinter import ttk, Frame, Entry, Scrollbar, messagebox
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from pandas import ExcelWriter, DataFrame
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
from datetime import datetime, date
from clipboard import copy
from json import load


class Funcoes:
    def iniciar_testes(self):
        # Coletando opções
        self.resp_squad = self.box_squad.get() if self.box_squad.get() != 'Todos os Squads' else 0
        self.salvar = self.box_salvar.get()
        self.sites = self.url_lps()
        self.resultado_etapas = []
        self.resultado_geral = dict()
        self.resultado_final = []

        # Desativando botões da interface
        self.box_salvar.configure(state='disable')
        self.box_squad.configure(state='disable')
        self.bt_iniciar.destroy()
        try:
            self.entry_destino_arquivo.configure(state='disable')
        except:
            pass
        # Meios técnicos para recriar o botão
        self.bt_iniciar = ttk.Button(self.frame_um, text='Testes Finalizados!', width=20, style=SUCCESS)
        self.bt_iniciar.pack(pady=(164, 0))

        # Alterando e inserindo elementos
        self.root.geometry('450x530')
        self.frame_um.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.4985)
        self.frame_2()
        self.frame_de_lista()

        #Iniciando o fluxo
        self.fluxo_completo()
        self.salvar_arquivo()

    def tratar_cidade(self, navegador):
        try:
            navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select').click()
            navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/select/option[2]').click()
            navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
            return 'Cidade OK'
        except:
            try:
                navegador.find_element(By.XPATH, '//*[@id="__next"]/section/div/div/main/section/div/select').click()
                navegador.find_element(By.XPATH,
                                       '//*[@id="__next"]/section/div/div/main/section/div/select/option[2]').click()
                return 'Cidade OK'
            except:
                try:
                    navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/div/div/div/select').click()
                    navegador.find_element(By.XPATH,
                                           '//*[@id="modal-portal"]/div/div/form/div/div/div/select/option[2]').click()
                    navegador.find_element(By.XPATH, '//*[@id="modal-portal"]/div/div/form/button').click()
                    return 'Cidade OK'
                except:
                    return 'N/A'
                    pass

    def abrir_snippet(self, navegador):
        try:
            sleep(1)
            navegador.execute_script('document.querySelector("#dots-cta > img").click()')  # clica snippet
            navegador.execute_script('document.querySelector("#dots-chat-cta > img").click()')  # clica no ícone webchat
            return 'Snippet OK'
        except:
            return 'Snippet Não OK'

    def url_lps(self):
        with open('url_lps.json', encoding='utf-8') as arquivo_urls:
            sites = load(arquivo_urls)
        return sites.copy()

    def mapeamento_steps(self, cep='30000000', numero='01', dt_vencimento='não sei'):
        with open('mapeamento_steps.json', encoding='utf-8') as mapeamento:
            palavras_chave = load(mapeamento)
        palavras_chave['CEP'].append(cep)
        palavras_chave['CEP_2'].append(cep)
        palavras_chave['Número Ende.'].append(numero)
        palavras_chave['Data Vencimento'].append(dt_vencimento)
        palavras_chave['Data Vencimento2'].append(dt_vencimento)

        return palavras_chave.copy()

    def encontra_chave_step(self, navegador, cep='30000000', numero='01', dt_vencimento='não sei'):
        steps_local = self.mapeamento_steps(cep, numero, dt_vencimento)
        cont = 0
        while True:
            n_bloco_atual = len(navegador.find_elements(By.XPATH, '//*[@id="messages-list"]/div[1]/div/div/div[2]/div'))
            if n_bloco_atual % 2 == 0 and n_bloco_atual > 0:
                try:
                    WebDriverWait(navegador, 1).until(
                        expected_conditions.presence_of_element_located(
                            (By.XPATH, f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual + 1}]')))
                except:
                    break
                else:
                    continue
            else:
                sleep(0.5)
                cont += 0.5
                if cont >= 1:
                    break

        n_ultima_msg = len(navegador.find_elements(
            By.XPATH, f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]/div[2]/div'))
        try:
            for cont in range(1, n_ultima_msg + 1):
                mensagem = str(navegador.find_element(
                    By.XPATH, f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]'
                              f'/div[2]/div[{cont}]/div/div/div/div/div[1]/div[1]').text)
                for key, valor in steps_local.items():
                    if valor[0].upper() in mensagem.upper():
                        return key
        except:
            return '1'
        else:
            return '1'

    def interacao_chat(self, navegador, operacao, CEP='30000000', num='01', dt_vencimento='não sei', squad_atual='Null'):
        steps = self.mapeamento_steps(CEP, num, dt_vencimento)
        lista_aux_chat = []
        tempo_erro = apoio = 0

        while True:
            chave_step = self.encontra_chave_step(navegador, CEP, num, dt_vencimento)
            if chave_step.isnumeric():
                tempo_erro += int(chave_step)
            elif apoio == chave_step:
                tempo_erro += 1
            else:
                lista_aux_chat.append(f'{chave_step} - OK')
                tempo_erro = 0

            if chave_step in 'Oferta Planos':
                sleep(3.5)

            try:
                navegador.find_element(By.ID, 'msg-textarea').send_keys(steps[chave_step][1], Keys.ENTER)
            except:
                pass
            n_bloco_atual = len(navegador.find_elements(By.XPATH, '//*[@id="messages-list"]/div[1]/div/div/div[2]/div'))
            n_ultima_msg = len(navegador.find_elements(
                By.XPATH, f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]/div[2]/div'))
            if chave_step.split()[0].upper() in 'ERRO':
                mensagem = str(navegador.find_element(
                    By.XPATH, f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]'
                              f'/div[2]/div[{n_ultima_msg - 1}]/div/div/div/div/div[1]/div[1]').text)
                self.lista_observacoes.insert('', END, values=(squad_atual, operacao, chave_step, mensagem))
                if self.salvar == 'Sim':
                    pasta_arquivo = self.entry_destino_arquivo.get()
                    navegador.save_screenshot(f'{pasta_arquivo}/{operacao} - {chave_step} ({date.today()}).png')
                break
            if chave_step in 'Consultor Indisponível, Finalização' or chave_step.split()[0].upper() in 'TRANSBORDO_ATH':
                break
            elif chave_step == '1' and n_bloco_atual % 2 == 0 and n_bloco_atual > 0 and tempo_erro >= 15:
                chave_step = 'Chave não mapeada'
                lista_aux_chat.append(chave_step)
                mensagem = str(navegador.find_element(
                    By.XPATH, f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]'
                              f'/div[2]/div[{n_ultima_msg - 1}]/div/div/div/div/div[1]/div[1]').text)
                self.lista_observacoes.insert('', END, values=(squad_atual, operacao, chave_step, mensagem))
                if self.salvar == 'Sim':
                    pasta_arquivo = self.entry_destino_arquivo.get()
                    navegador.save_screenshot(f'{pasta_arquivo}/{operacao} - {chave_step} ({date.today()}).png')
                break
            elif n_bloco_atual > 0 and tempo_erro >= 15:
                chave_step = f'ERROR TIMEOUT'
                lista_aux_chat.append(chave_step)
                mensagem = str(navegador.find_element(
                    By.XPATH, f'//*[@id="messages-list"]/div[1]/div/div/div[2]/div[{n_bloco_atual}]'
                              f'/div[2]/div[{n_ultima_msg - 1}]/div/div/div/div/div[1]/div[1]').text)
                self.lista_observacoes.insert('', END, values=(squad_atual, operacao, chave_step, mensagem))
                if self.salvar == 'Sim':
                    pasta_arquivo = self.entry_destino_arquivo.get()
                    navegador.save_screenshot(f'{pasta_arquivo}/{operacao} - {chave_step} ({date.today()}).png')
                break
            apoio = chave_step
        return lista_aux_chat[:]

    def fluxo_completo(self):
        #try:
        self.navegador = Chrome()
        lista_auxiliar = []
        if self.resp_squad == 0:
            nome_squad_1 = list(self.sites)[0]
            nome_lp_1 = list(self.sites[nome_squad_1])[0]
            primeira_url = self.sites[nome_squad_1][nome_lp_1][0]
            for k, squad in self.sites.items():
                for k2, lp in squad.items():
                    self.resultado_geral[k2] = []
                    try:
                        if self.sites[k][k2][0] == primeira_url:
                            self.navegador.get(lp[0])
                        else:
                            self.navegador.switch_to.new_window('tab')
                            self.navegador.get(lp[0])
                    except:
                        self.resultado_geral[k2] = ['LP Fora do Ar']
                        self.lista_observacoes.insert('', END, values=(k, k2,
                                                                       'LP Fora do Ar', 'LP Fora do Ar'))
                        continue
                    else:
                        c = self.sites[k][k2][1]
                        n = self.sites[k][k2][2]
                        venci = 'Não sei'
                        try:
                            venci = self.sites[k][k2][3]
                        except:
                            pass
                        self.resultado_etapas.append('LP OK')
                        self.resultado_etapas.append(self.tratar_cidade(self.navegador))
                        self.resultado_etapas.append(self.abrir_snippet(self.navegador))
                        try:
                            self.navegador.switch_to.frame(self.navegador.find_element(By.ID, 'blip-chat-iframe'))
                            WebDriverWait(self.navegador, 30).until(
                                expected_conditions.presence_of_element_located(
                                    (By.XPATH,
                                     '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div')))
                        except:
                            self.resultado_etapas.append('CHAT TIMEOUT')
                            for cont in range(0, len(lista_auxiliar)):
                                self.resultado_geral[k2].append(self.resultado_etapas[cont])
                            if self.resultado_etapas[-1] == 'Snippet Não OK':
                                self.lista_observacoes.insert('', END, values=(k, k2,
                                                                               'Snippet Não OK', 'CHAT TIMEOUT'))
                            self.resultado_etapas.clear()
                            continue
                        else:
                            self.resultado_etapas.append('CHAT OK')

                        lista_auxiliar = self.interacao_chat(self.navegador, k2, c, n, venci, k)
                        for cont in range(0, len(lista_auxiliar)):
                            self.resultado_etapas.append(lista_auxiliar[cont])

                        self.resultado_geral[k2] = self.resultado_etapas[:]
                        self.resultado_etapas.clear()
                        lista_auxiliar.clear()

                tamanho_maximo_etapas = 0
                for operacao in self.resultado_geral.values():
                    if len(operacao) > tamanho_maximo_etapas:
                        tamanho_maximo_etapas = len(operacao)

                for operacao in self.resultado_geral.values():
                    if len(operacao) < tamanho_maximo_etapas:
                        dif = tamanho_maximo_etapas - len(operacao)
                        for cont in range(0, dif):
                            operacao.append('-')

                vars()[f'df_{k}'] = DataFrame(data=self.resultado_geral)
                self.resultado_geral.clear()
                self.resultado_final.append(vars()[f'df_{k}'])

        else:
            nome_lp_1 = list(self.sites[self.resp_squad])[0]
            primeira_url = self.sites[self.resp_squad][nome_lp_1][0]
            for k2, lp in self.sites[self.resp_squad].items():
                self.resultado_geral[k2] = []
                try:
                    if lp[0] == primeira_url:
                        self.navegador.get(lp[0])
                    else:
                        self.navegador.switch_to.new_window('tab')
                        self.navegador.get(lp[0])
                except:
                    self.resultado_geral[k2] = ['LP Fora do Ar']
                    self.lista_observacoes.insert('', END, values=(self.resp_squad, k2,
                                                                   'LP Fora do Ar', 'LP Fora do Ar'))
                else:
                    c = self.sites[self.resp_squad][k2][1]
                    n = self.sites[self.resp_squad][k2][2]
                    venci = 'Não sei'
                    try:
                        venci = self.sites[self.resp_squad][k2][3]
                    except:
                        pass
                    self.resultado_etapas.append('LP OK')
                    self.resultado_etapas.append(self.tratar_cidade(self.navegador))
                    self.resultado_etapas.append(self.abrir_snippet(self.navegador))
                    try:
                        self.navegador.switch_to.frame(self.navegador.find_element(By.ID, 'blip-chat-iframe'))
                        WebDriverWait(self.navegador, 30).until(
                            expected_conditions.presence_of_element_located(
                                (By.XPATH,
                                 '//*[@id="messages-list"]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]/div')))
                    except:
                        self.resultado_etapas.append('CHAT TIMEOUT')
                        for cont in range(0, len(lista_auxiliar)):
                            self.resultado_geral[k2].append(self.resultado_etapas[cont])
                        if self.resultado_etapas[-1] == 'Snippet Não OK':
                            self.lista_observacoes.insert('', END, values=(self.resp_squad, k2,
                                                                           'Snippet Não OK', 'CHAT TIMEOUT'))
                        self.resultado_etapas.clear()
                        continue
                    else:
                        self.resultado_etapas.append('CHAT OK')

                    lista_auxiliar = self.interacao_chat(self.navegador, k2, c, n, venci, self.resp_squad)
                    for cont in range(0, len(lista_auxiliar)):
                        self.resultado_etapas.append(lista_auxiliar[cont])

                    self.resultado_geral[k2] = self.resultado_etapas[:]
                    self.resultado_etapas.clear()
                    lista_auxiliar.clear()

            tamanho_maximo_etapas = 0
            for operacao in self.resultado_geral.values():
                if len(operacao) > tamanho_maximo_etapas:
                    tamanho_maximo_etapas = len(operacao)

            for operacao in self.resultado_geral.values():
                if len(operacao) < tamanho_maximo_etapas:
                    dif = tamanho_maximo_etapas - len(operacao)
                    for cont in range(0, dif):
                        operacao.append('-')

            vars()[f'df_{self.resp_squad}'] = DataFrame(data=self.resultado_geral)
            self.resultado_geral.clear()
            self.resultado_final.append(vars()[f'df_{self.resp_squad}'])

        r"""except Exception as erro:
            messagebox.showerror(title='Erro no fluxo', message=f'Houve erro no fluxo do chat!\n\n'
                                                                f'Erro: {erro.__class__}\n\n'
                                                                f'Descrição: {erro.__context__}\n'
                                                                f'{erro.__str__()}')"""

    def salvar_arquivo(self):
        #try:
        if self.salvar == 'Sim':
            hora = int(str(datetime.time(datetime.today()))[:2])
            if 12 > hora >= 6:
                turno = 'Manhã'
            elif 18 > hora >= 12:
                turno = 'Tarde'
            else:
                turno = 'Noite'
            pasta_arquivo = self.entry_destino_arquivo.get() + '/'
            pasta_arquivo = f'{pasta_arquivo}/Testes de Fluxo {self.resp_squad if self.resp_squad != 0 else ""}' \
                            f' {date.today().day}-{date.today().month} ({turno}).xlsx'
            arquivo = ExcelWriter(pasta_arquivo, engine='xlsxwriter')
            if self.resp_squad == 0:
                for i, resultado in enumerate(self.resultado_final):
                    nome = list(self.sites)[i]
                    self.resultado_final[i].to_excel(arquivo, sheet_name=nome, index=False)
            else:
                self.resultado_final[0].to_excel(arquivo, sheet_name=self.resp_squad, index=False)
            arquivo.save()
        self.resultado_final.clear()
        r"""except Exception as erro:
            messagebox.showerror(title='Erro no Salvamento', message=f'Houve erro ao salvar os testes!\n\n'
                                                                f'Erro: {erro.__class__}\n\n'
                                                                f'Descrição: {erro.__context__}\n'
                                                                f'{erro.__str__()}')"""


class Janela_principal(Funcoes):
    def __init__(self):
        # Atributos

        #Estilo
        self.estilo_1 = Style(theme='cosmo')
        self.estilo_1.configure('TButton', font='sans-serif 11')
        self.estilo_1.configure('Treeview', foreground='#3D3D3D', rowheight=25)
        self.estilo_1.map('Treeview', background=[('selected', 'green')])
        #Opções comboBox squad
        self.squads = ['Todos os Squads']
        aux = list(Funcoes.url_lps(self))
        num_squads = len(aux)
        for x in range(0, num_squads):
            self.squads.append(aux[x])
        # Define tema e cria o objeto janela
        self.root = self.estilo_1.master
        # Funções
        self.janela()
        self.frame_1()
        self.titulo()
        self.campos()
        self.botoes()
        # Mantendo janela aberta
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
        self.frame_dois = ttk.LabelFrame(self.root, text=' Observações ')
        self.frame_dois.place(relx=0.02, rely=0.52, relwidth=0.96, relheight=0.465)

    def frame_de_lista(self):
        # Barra de Rolagem vertical
        self.scroll_vertical = Scrollbar(self.frame_dois, orient='vertical')
        self.scroll_vertical.place(relx=0.92, rely=0.01, relwidth=0.07, relheight=0.88)
        # Barra de Rolagem horizontal
        self.scroll_horizontal = Scrollbar(self.frame_dois, orient='horizontal')
        self.scroll_horizontal.place(relx=0.01, rely=0.9, relwidth=0.9, relheight=0.08)
        #Criando o frame com o nome das colunas e linkando-o aos scrolls
        self.lista_observacoes = ttk.Treeview(self.frame_dois, height=2, columns=('squad', 'operação', 'observação', 'mensagem'),
                                              show='headings',
                                              yscrollcommand=self.scroll_vertical.set,
                                              xscrollcommand=self.scroll_horizontal.set)
        self.lista_observacoes.place(relx=0.01, rely=0.01, relwidth=0.9, relheight=0.88)
        # Linkando a barra de rolagem e a lista
        self.scroll_vertical.config(command=self.lista_observacoes.yview)
        self.scroll_horizontal.config(command=self.lista_observacoes.xview)
        #Cabeçalho das colunas
        #self.lista_generica.heading('#0', text='')
        self.lista_observacoes.heading('#1', text='Squad', anchor=W)
        self.lista_observacoes.heading('#2', text='Operação', anchor=W)
        self.lista_observacoes.heading('#3', text='Observação', anchor=W)
        self.lista_observacoes.heading('#4', text='Mensagem', anchor=W)
        #Tamanho das colunas
        self.lista_observacoes.column('#1', width=80, anchor=W)
        self.lista_observacoes.column('#2', width=80, anchor=W)
        self.lista_observacoes.column('#3', width=100, anchor=W)
        self.lista_observacoes.column('#4', width=240, anchor=W)
        #for x in range(1, 8):
        #    self.lista_observacoes.insert('', END, values=('EVA', 'LIGUE', 'ERROR TIMEOUT', 'TESTE TESTE TESTE TESTE TESTE TESTE'))
        #    self.lista_observacoes.insert('', END, values=('WALL-E', 'TESTE', 'ERROR TIMEOUT', 'TESTE TESTE TESTE TESTE TESTE TESTE'))

    def titulo(self):
        self.titulo_lb = ttk.Label(self.frame_um, text='BOT de Teste de Fluxo LP', font=('sans-serif', '18', 'bold'),
                                   foreground='#257DFE')
        self.titulo_lb.pack(pady=8)

    def campos(self):
        # Campo Squad
        self.lb_squad = ttk.Label(self.frame_um, text='Escolha o Squad:', font=('sans-serif', '13'), foreground='black')
        self.lb_squad.place(relx=0.02, rely=0.265)
        # Combobox
        self.box_squad = ttk.Combobox(
            self.frame_um, values=self.squads, font=('sans-serif', '13'),
            foreground='black', state='readonly', takefocus=False
        )
        self.box_squad.current(0)
        self.box_squad.place(relx=0.35, rely=0.24, relwidth=0.625)

        # Campo "Salvar""
        self.lb_salvar = ttk.Label(self.frame_um, text='Deseja Salvar o resultado?', font=('sans-serif', '13'),
                                   foreground='black')
        self.lb_salvar.place(relx=0.02, rely=0.45)
        # Combobox
        self.box_salvar = ttk.Combobox(
            self.frame_um, values=['Sim', 'Não'], font=('sans-serif', '13'), foreground='black', state='readonly',
            takefocus=False
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
            # Campo de destino do arquivo
            self.entry_destino_arquivo = Entry(self.frame_um, font=('sans-serif', 9), fg='gray', state='normal')
            self.entry_destino_arquivo.place(relx=0.375, rely=0.615, relwidth=0.60, relheight=0.12)
            self.entry_destino_arquivo.insert('1',
                                            'S:/Inovação/Planejamento/3 - MIS/Gerencial/Acompanhamento das ISPS - Semanal/Testes de Fluxo')
        else:
            try:
                self.lb_destino_arquivo.destroy()
                self.entry_destino_arquivo.destroy()
            except:
                pass

    def copiar_dados_lista(self):
        try:
            valores = list()
            itens_selecionados = self.lista_observacoes.selection()
            for i_item in range(0, len(itens_selecionados)):
                valores.append(self.lista_observacoes.item(itens_selecionados[i_item], 'values'))
            for cont in range(0, len(itens_selecionados)):
                pass
            copy(valores)
        except:
            messagebox.showinfo(title='ERRO', message='Selecione um elemento para ser obtido.')


Janela_principal()
