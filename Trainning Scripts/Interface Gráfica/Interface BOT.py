from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from ttkbootstrap.constants import *
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import datetime


class Funcoes:
    def iniciar_testes(self):
        # Coletando opções
        self.resp = self.box_squad.get() if self.box_squad.get() != 'Todos os Squads' else 0
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
        self.bt_iniciar = ttk.Button(self.frame_um, text='Testes Finalizados!', width=20, style=WARNING)
        self.bt_iniciar.pack(pady=(162, 0))

        # Alterando e inserindo elementos
        '''self.root.geometry('450x750')
        self.frame_um.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.35)
        self.frame_2()
        self.frame_3()'''

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
        sites = {'EVA': {#'BLINK': ['https://ofertasblinktelecom.com.br/', '31235060', '148'],
                         #'BRISANET': ['https://ofertasbrisanet.com.br', '59607571', '241'],
                         #'TELY': ['https://ofertastely.com.br/', '58038000', '315'],
                         'LIGUE': ['https://ofertasligue.net/', '87005002', '405']#,
                         #'SUMICITY': ['https://ofertassumicity.com.br/', '27534240', '382']#,
                         #'VIP': ['https://ofertasvipbrtelecom.com.br/', '09415110', '16']
                         },

                 'WALL-E': {'TVN': ['https://ofertastvn.com.br', '65082223', '13']#,
                            #'COPREL': ['http://ofertascoprel.com.br/', '98280000', '175'],
                            #'DESKTOP': ['https://desktop-fibra-internet.com.br/', '11712020', '315'],
                            #'MASTER': ['https://ofertassoumaster.com.br/', '38616072', '22'],
                            #'AZZA': ['https://ofertasazza.net.br/', '18071724', '65'],
                            #'FLEETNET': ['https://ofertasfleetnet.com.br/', '19026410', '885'],
                            #'SOCITEL': ['https://mkt.azza.net.br/socitel', '06770300', '350'],
                            #'INFOVALE': ['http://ofertasinfovaletelecom.com.br/', '11925000', '710']
                            },

                 'BURN-E': {'MOB': ['http://ofertasmobtelecom.com.br/', '60525200', '150', '5']#,
                            #'WECLIX': ['http://ofertasweclix.com.br', '14807049', '60', '5'],
                            #'CABONNET': ['https://ofertascabonnet.com.br/', '19042410', '347', '5'],
                            #'SERCOMTEL': ['http://ofertasercomtel.com.br/', '86055630', '995'],
                            #'PROXXIMA': ['https://ofertastoolsnet.com.br/', '59575000', '07', '5']
                            },

                 'M-O': {'VALENET': ['https://ofertasvalenet.com.br/', '31930560', '120']#,
                         #'COPEL': ['https://ofertascopeltelecom.com.br/', '86320970', '50', '5'],
                         #'ALGAR': ['https://ofertasalgartelecom.com.br/', '38407261', '295', '3'],
                         #'MHNET': ['https://ofertasmhnet.com.br/', '84032602', '34']
                         }}
        return sites.copy()

    def mapeamento_steps(self, cep='30000000', numero='01', dt_vencimento='não sei'):
        palavras_chave = {'ERRO Geral': ['Ocorreu um erro'],  # Erro geral
                          'ERRO Compreensão': ['Não entendi'],  # Erro de compreensão da mensagem enviada
                          'ERRO Viabilidade': ['Estou com problemas'],  # Erro de busca de viabilidade
                          'ERRO Busca CEP': ['Não encontrei nenhum endereço'],  # Erro na busca de CEP
                          'ERRO Transbordo Precoce': ['não consegui te entender'],
                          # Erro de transbordo antes do fim do fluxo
                          'Outro Endereço': ['Gostaria de solicitar para outro endereço?', 'Transbordar para ATH'],
                          'Consultor Indisponível': ['Os nossos consultores estão disponíveis das'],
                          'Finalização': ['Estamos finalizando o seu atendimento'],
                          'Já sou Cliente': ['Você já é nosso cliente?', 'Não'],
                          'Tipo Endereço': ['Selecione o tipo do endereço', 'Casa'],
                          'Área Rural': ['em uma área rural', 'Não'],
                          'Condominio': ['localizado em um condomínio', 'Não'],
                          'CEP': ['digite o seu CEP', cep],
                          'CEP_2': ['digite seu CEP', cep],
                          'Número Ende.': ['o número do endereço', numero],
                          'Complemento': ['o complemento do endereço', 'não'],
                          'Prédio': ['se encontra em um prédio', 'Não'],
                          'Bairro': ['nome do bairro', 'NuloTeste'],
                          'Rua': ['o nome da rua', 'NuloTeste'],
                          'Referência': ['Informe um ponto de referência do endereço', 'Não'],
                          'Referência2': ['Qual o ponto de referência do endereço', 'Não'],
                          'Confirma endereço': ['Está correto?', 'Sim'],
                          'Oferta Planos': ['Escolha uma das opções abaixo que melhor te atende:', 1],
                          'Adicionar produtos': ['adicionar mais produtos ao seu carrinho', 'Agora não'],
                          'TV': ['adicionar TV', 'Não'],
                          'Tel Fixo': ['Telefone Fixo ao seu carrinho', 'Não'],
                          'Tel Móvel': ['Telefone Móvel ao seu carrinho', 'Não'],
                          'Nome': ['seu nome completo', 'BOT de Teste de Fluxo'],
                          'CPF': ['o seu CPF', '96315157459'],
                          'RG': ['número do seu RG', '00000000'],
                          'Data Nascimento': ['data de nascimento', '01/01/2000'],
                          'Nome Mãe': ['nome da sua mãe', 'Teste Nome Mãe'],
                          'Gênero': ['me informe o seu gênero', 'Não binário'],
                          'Estado Civil': ['estado civil', 'Solteiro'],
                          'Profissão': ['sua profissão atual', 'BOT Analista de Fluxo'],
                          'Telefone Princ': ['número preferível', '31955555555'],
                          'Telefone Princ2': ['seu melhor número', '31955555555'],
                          'Telefone Adic': ['número adicional', '31966666666'],
                          'Envio Boleto': ['como deseja receber seu boleto', 'E-mail'],
                          'E-mail': ['seu e-mail', 'nulonulo@gmail.com'],
                          'Provedora': ['alguma provedora de internet', 'Não'],
                          'Promoção': ['outra operadora de internet', 'Não'],
                          'Pagamento': ['pagamento por boleto digital ou por débito em conta', 'Boleto Digital'],
                          'Pagamento2': ['Qual o melhor método de pagamento pra você?', 'Boleto Online'],
                          'Pagamento3': ['prefere realizar o pagamento por', 'Boleto'],
                          'Data Vencimento': ['datas de vencimento disponíveis', dt_vencimento],
                          'Data Vencimento2': ['melhor data de vencimento pra você', dt_vencimento],
                          'Turno Inst.': ['o turno ideal para a instalação', 'Manhã'],
                          'Confirma Pedido': ['Preciso que você confirme as seguintes informações', 'Não Confirmo'],
                          'Confirma Pedido2': ['Você confirma as informações acima?', 'Não Confirmo'],
                          'Motivo não confirmação': ['Você não confirmou por qual motivo?', 'Falar com humano'],
                          'Transbordo ATH': ['um consultor especializado',
                                             'Favor finalizar como teste. Tenha um ótimo trabalho!'],
                          'Transbordo ATH2': ['Vou te transferir para',
                                              'Favor finalizar como teste. Tenha um ótimo trabalho!']
                          }
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

    def interacao_chat(self, navegador, operacao, CEP='30000000', num='01', dt_vencimento='não sei'):
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
            if chave_step.split()[0].upper() in 'ERRO':
                navegador.save_screenshot(
                    f'S:/Inovação/Planejamento/3 - MIS/Gerencial/Acompanhamento das ISPS - Semanal/Testes de Fluxo/prints/'
                    f'{operacao} - {chave_step} ({datetime.date.today()}).png')

            n_bloco_atual = len(navegador.find_elements(By.XPATH, '//*[@id="messages-list"]/div[1]/div/div/div[2]/div'))
            if chave_step in 'Transbordo ATH, Consultor Indisponível, Finalização':
                break
            elif chave_step == '1' and n_bloco_atual % 2 == 0 and n_bloco_atual > 0 and tempo_erro >= 15:
                chave_step = 'Chave não mapeada'
                lista_aux_chat.append(chave_step)
                navegador.save_screenshot(
                    f'S:/Inovação/Planejamento/3 - MIS/Gerencial/Acompanhamento das ISPS - Semanal/Testes de Fluxo/prints/'
                    f'{operacao} - {chave_step} ({datetime.date.today()}).png')
                break
            elif n_bloco_atual > 0 and tempo_erro >= 15:
                chave_step = f'ERROR TIMEOUT'
                lista_aux_chat.append(chave_step)
                navegador.save_screenshot(
                    f'S:/Inovação/Planejamento/3 - MIS/Gerencial/Acompanhamento das ISPS - Semanal/Testes de Fluxo/prints/'
                    f'{operacao} - {chave_step} ({datetime.date.today()}).png')
                break
            apoio = chave_step
        return lista_aux_chat[:]

    def salvar_arquivo(self):
        if self.salvar == 'Sim':
            hora = int(str(datetime.datetime.time(datetime.datetime.today()))[:2])
            if 12 > hora >= 6:
                turno = 'Manhã'
            elif 18 > hora >= 12:
                turno = 'Tarde'
            else:
                turno = 'Noite'
            pasta_arquivo = self.entry_destino_arquivo.get()
            pasta_arquivo = f'{pasta_arquivo}/Testes de Fluxo {self.resp if self.resp != 0 else ""} ' \
                            f'{datetime.date.today().day}-{datetime.date.today().month} ({turno}).xlsx'
            arquivo = pd.ExcelWriter(pasta_arquivo, engine='xlsxwriter')
            if self.resp == 0:
                for i, resultado in enumerate(self.resultado_final):
                    self.resultado_final[i].to_excel(arquivo, sheet_name=i, index=False)
            else:
                self.resultado_final[0].to_excel(arquivo, sheet_name=self.resp, index=False)
            arquivo.save()
        self.resultado_final.clear()

    def fluxo_completo(self):
        self.navegador = Chrome()
        lista_auxiliar = []
        if self.resp == 0:
            for k, squad in self.sites.items():
                for k2, lp in squad.items():
                    print('\033[1:33m-' * 40, end='\033[m\n')
                    print(f'Estou iniciando os testes na \033[1:34m{k2}\033[m.')
                    self.resultado_geral[k2] = []
                    try:
                        if self.sites[k][k2][0] == 'https://ofertasblinktelecom.com.br/':
                            self.navegador.get(lp[0])
                        else:
                            self.navegador.switch_to.new_window('tab')
                            self.navegador.get(lp[0])
                    except:
                        self.resultado_geral[k2] = ['LP Fora do Ar']
                        print('Teste finalizado com falha no carregamento da LP!')
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
                                self.resultado_etapas.append(lista_auxiliar[cont])
                            continue
                        else:
                            self.resultado_etapas.append('CHAT OK')

                        lista_auxiliar = self.interacao_chat(self.navegador, k2, c, n, venci)
                        for cont in range(0, len(lista_auxiliar)):
                            self.resultado_etapas.append(lista_auxiliar[cont])

                        self.resultado_geral[k2] = self.resultado_etapas[:]
                        self.resultado_etapas.clear()
                        lista_auxiliar.clear()
                        print('Teste finalizado com êxito!')

                tamanho_maximo_etapas = 0
                for operacao in self.resultado_geral.values():
                    if len(operacao) > tamanho_maximo_etapas:
                        tamanho_maximo_etapas = len(operacao)

                for operacao in self.resultado_geral.values():
                    if len(operacao) < tamanho_maximo_etapas:
                        dif = tamanho_maximo_etapas - len(operacao)
                        for cont in range(0, dif):
                            operacao.append('-')

                vars()[f'df_{k}'] = pd.DataFrame(data=self.resultado_geral)
                self.resultado_geral.clear()
                self.resultado_final.append(vars()[f'df_{k}'])

        else:
            for k2, lp in self.sites[self.resp].items():
                self.resultado_geral[k2] = []
                try:
                    print('\033[1:33m-' * 40, end='\033[m\n')
                    print(f'Estou iniciando os testes na \033[1:34m{k2}\033[m.')
                    if k2 in 'BLINK TVN MOB VALENET':
                        self.navegador.get(lp[0])
                    else:
                        self.navegador.switch_to.new_window('tab')
                        self.navegador.get(lp[0])
                except:
                    self.resultado_geral[k2] = ['LP Fora do Ar']
                    print('Teste finalizado com falha no carregamento da LP!')
                else:
                    c = self.sites[self.resp][k2][1]
                    n = self.sites[self.resp][k2][2]
                    venci = 'Não sei'
                    try:
                        venci = self.sites[self.resp][k2][3]
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
                        continue
                    else:
                        self.resultado_etapas.append('CHAT OK')

                    lista_auxiliar = self.interacao_chat(self.navegador, k2, c, n, venci)
                    for cont in range(0, len(lista_auxiliar)):
                        self.resultado_etapas.append(lista_auxiliar[cont])

                    self.resultado_geral[k2] = self.resultado_etapas[:]
                    self.resultado_etapas.clear()
                    lista_auxiliar.clear()
                    print('Teste finalizado com êxito!')

            tamanho_maximo_etapas = 0
            for operacao in self.resultado_geral.values():
                if len(operacao) > tamanho_maximo_etapas:
                    tamanho_maximo_etapas = len(operacao)

            for operacao in self.resultado_geral.values():
                if len(operacao) < tamanho_maximo_etapas:
                    dif = tamanho_maximo_etapas - len(operacao)
                    for cont in range(0, dif):
                        operacao.append('-')

            vars()[f'df_{self.resp}'] = pd.DataFrame(data=self.resultado_geral)
            self.resultado_geral.clear()
            self.resultado_final.append(vars()[f'df_{self.resp}'])


class Janela_principal(Funcoes):
    def __init__(self):
        # Atributos
        self.estilo_1 = Style(theme='cosmo')
        # ttk.Style().configure('TEntry')
        ttk.Style().configure('TButton', font='sans-serif 10')
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
        # Campo Squad
        self.lb_squad = ttk.Label(self.frame_um, text='Escolha o Squad:', font=('sans-serif', '13'), foreground='black')
        self.lb_squad.place(relx=0.02, rely=0.265)
        # Combobox
        self.box_squad = ttk.Combobox(
            self.frame_um, values=['Todos os Squads', 'EVA', 'WALL-E', 'BURN-E', 'M-O'], font=('sans-serif', '13'),
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


Janela_principal()
