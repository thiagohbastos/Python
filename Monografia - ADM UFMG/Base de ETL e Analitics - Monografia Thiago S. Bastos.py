#%%
# --------------- IMPORTANDO BIBLIOTECAS NECESSÁRIAS ---------------
#Cotações do Yahoo Finance
import yfinance as yf

# Tratamento de Dados
import requests
import json
import numpy as np
import scipy as sp
import statsmodels.api as sm
#import sklearn as sk
import pandas as pd
from pandas.tseries.offsets import BDay
pd.set_option("display.max_colwidth", 150)

#Gráficos
#import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

#Utilidades
from datetime import date
import IPython

pd.options.display.float_format = '{:.4f}'.format
pd.set_option("display.max_colwidth", 150)




#%% Funções
# --------------- CRIANDO FUNÇÕES ÚTEIS ---------------

def consulta_fundo(informes, cnpj):
    fundo = informes[informes['CNPJ_FUNDO'] == cnpj].copy()
    fundo.set_index('DT_COMPTC', inplace=True)
    fundo['cotas_normalizadas'] = (fundo['VL_QUOTA'] / fundo['VL_QUOTA'].iloc[0])*100
    return fundo

def busca_cadastro_cvm():
    try:
        url = 'http://dados.cvm.gov.br/dados/FI/CAD/DADOS/cad_fi.csv'
        return pd.read_csv(url, sep=';', encoding='ISO-8859-1')
    except:
        print("Arquivo {} não encontrado!".format(url))

def gera_base_volume(df_base, columns_groupby:list):
    df_resultado = df_base.groupby(columns_groupby).agg({'CAPTC_DIA': ['sum']
                                , 'RESG_DIA':['sum']})

    df_resultado['VOLUME'] = df_resultado['CAPTC_DIA']['sum'] - df_resultado['RESG_DIA']['sum']

    for i, v in enumerate(columns_groupby):
        df_resultado[v] = df_resultado.index.get_level_values(i)

    df_resultado = df_resultado.reset_index(drop=True)

    df_resultado['PERIODO'] = ['Pré-pandêmico' 
                            if x[0] in(2017, 2018, 2019) 
                            or (x[0] == 2020 and x[1] in (1, 2))
                            else 'Pandêmico'
                            for x in df_resultado[['ANO', 'MES']].values
                            ]
    df_resultado['DATA'] = [str(int(x[0])) 
                            + '-' 
                            + ('0' * (2 - len(str(int(x[1])))))
                            + str(int(x[1]))
                            for x in df_resultado[['ANO', 'MES']].values]
    df_resultado = df_resultado.sort_values(by='DATA').reset_index(drop=True)
    return df_resultado

def gera_base_rentabilidade(df_base, columns_groupby:list, coluna_foco):
    df_resultado = df_base.groupby(columns_groupby).agg({'VL_QUOTA': 'mean'})
    df_resultado['RENTABILIDADE'] = df_resultado.groupby(coluna_foco)['VL_QUOTA'].pct_change()*100

    for i, v in enumerate(columns_groupby):
        df_resultado[v] = df_resultado.index.get_level_values(i)
    df_resultado = df_resultado.reset_index(drop=True)

    df_resultado.dropna(subset=['RENTABILIDADE'], inplace=True)

    df_resultado['DATA'] = [str(int(x[0])) 
                    + '-' 
                    + ('0' * (2 - len(str(int(x[1])))))
                    + str(int(x[1]))
                    for x in df_resultado[['ANO', 'MES']].values]

    df_resultado = df_resultado.sort_values(by='DATA').reset_index(drop=True)

    df_resultado['PERIODO'] = ['Pré-pandêmico' 
                        if x[0] in(2017, 2018, 2019) 
                        or (x[0] == 2020 and x[1] in (1, 2))
                        else 'Pandêmico'
                        for x in df_resultado[['ANO', 'MES']].values
                        ]
    df_resultado["MEDIA"] = df_resultado.groupby(["ANO", "MES"])["RENTABILIDADE"].transform("mean")
    return df_resultado



#%%
# --------------- EXTRAINDO VALORES DE BENCHMARK ---------------
data_inicio="2017-01-01"
data_fim="2022-12-31"

ibov = yf.download('^BVSP', start=data_inicio, end=data_fim)['Adj Close']
ibov = pd.DataFrame(ibov)

#.droplevel(1, axis=1)
ibov['DATA'] = ibov.index.get_level_values(0)
ibov.reset_index(drop=True, inplace=True)
ibov.rename(columns={'Adj Close': 'IBOVESPA'}, inplace=True)




#%% 
# --------------- TRATANDO CADASTRO DE FUNDOS GENÉRICOS E DE AÇÕES ---------------
cadastro_original = busca_cadastro_cvm()
cadastro = cadastro_original.copy()
cadastro = cadastro[cadastro['CLASSE'] == 'Fundo de Ações']
cadastro_cnpj = cadastro[['CNPJ_FUNDO'
                        , 'CLASSE_ANBIMA'
                        , 'PUBLICO_ALVO'
                        , 'SIT'
                        , 'INVEST_CEMPR_EXTER']]




#%%
# --------------- EXTRAINDO INFORMES DIÁRIOS DA CVM ---------------
df_informes = pd.read_csv('DF_INFORMES.csv', sep=';')
df_fundos_analisados = pd.DataFrame(df_informes['CNPJ_FUNDO'].drop_duplicates().reset_index(drop=True))
#periodo_y = range(2017, 2023)
#periodo_m = [x for x in range(1, 13)]
#periodo = []
#df_informes = pd.DataFrame()
#
#for ano in periodo_y:
#        for mes in periodo_m:
#                periodo.append('inf_diario_fi_{:02d}{:02d}.csv'.format(ano, mes))
#
#for x in periodo:
#        df_informes = pd.concat([df_informes
#                                                                    , pd.read_csv(x, sep=';', encoding='latin')]
#                                                                    , ignore_index=True)




#%%
# --------------- FILTRANDO APENAS OS INFORMES DE FUNDOS DE AÇÕES DE VAREJO ---------------
#df_informes = df_informes[df_informes['NR_COTST'] >= 500]
#df_informes = df_informes.merge(cadastro_cnpj, how='inner', on='CNPJ_FUNDO')
#df_informes['MES'] = [int(x[5:7]) for x in df_informes['DT_COMPTC']]
#df_informes['ANO'] = [int(x[:4]) for x in df_informes['DT_COMPTC']]

# CRIANDO BKP DOS INFORMES COMPLETOS
bkp = df_informes.copy()
df_informes.to_csv('df_informes.csv', sep=';', index=False)




#%%
# --------------- INICIANDO TRATAMENTO PARA VALIDAÇÃO DE H1 ---------------
# H1: A pandemia do COVID-19 reduziu o volume de investimentos em fundos de ações no Brasil,
# em comparação com o período pré-pandêmico.
df_H1 = gera_base_volume(df_base=df_informes, columns_groupby=['MES', 'ANO'])


#%%
# --------------- 1ª AVALIAÇÃO GRÁFICA DE H1 ---------------
sns.lineplot(data=df_H1, x=df_H1.index, y='VOLUME', hue="PERIODO", linewidth=3)
plt.title("Evolução do volume de investimentos por mês")
plt.xlabel("Meses Corridos (01/2017 à 12/2022)")
plt.ylabel("Volume de investimentos/mês (Bilhões R$)")

plt.axvline(0, color='black', linestyle='dotted' , linewidth=0.8)
plt.axvline(12, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(24, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(36, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(38, color='red', linestyle='dotted', linewidth=1)
plt.axvline(48, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(60, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(72, color='black', linestyle='dotted', linewidth=0.8)

plt.show()


#%%
# --------------- MÁXIMO E MÍNIMO DE H1 ---------------
# obtendo os valores máximos e mínimos da coluna VOLUME
h1_max_value = df_H1["VOLUME"].max()
h1_min_value = df_H1["VOLUME"].min()

# obtendo os índices dos valores máximos e mínimos da coluna VOLUME
h1_max_index = df_H1["VOLUME"].idxmax()
h1_min_index = df_H1["VOLUME"].idxmin()

# obtendo os valores da coluna MES correspondentes aos valores máximos e mínimos da coluna VOLUME
h1_max_month = df_H1.loc[h1_max_index, "DATA"]
h1_min_month = df_H1.loc[h1_min_index, "DATA"]


#%%
# --------------- 2ª AVALIANÇÃO GRÁFICA DE H1 ---------------
# OBTENDO VALORES RESUMIDOS DA AVALIAÇÃO GRÁFICA
resumo_H1 = df_H1[~df_H1['DATA'].isin(['2017-01', '2017-02'])]
resumo_H1 = resumo_H1.droplevel(1, axis=1).groupby('PERIODO').agg({'VOLUME': 'sum'})
resumo_H1.reset_index(inplace=True)
resumo_H1 = resumo_H1.iloc[[1, 0]]
sns.barplot(data=resumo_H1, x='PERIODO', y='VOLUME', hue='PERIODO')
plt.title("Somatório do Volume por Período")
plt.xlabel("Periodo")
plt.ylabel("Volume de investimentos/mês (Bilhões R$^(1/10))")
plt.show()



#%%

#%%
# --------------- INICIANDO TRATAMENTO PARA VALIDAÇÃO DE H2 ---------------
# H2: A pandemia do COVID-19 reduziu a rentabilidade dos fundos de ações no Brasil, 
# em comparação com o período pré-pandêmico.
df_H2 = gera_base_rentabilidade(df_base=df_informes
                                , columns_groupby=['CNPJ_FUNDO','ANO', 'MES']
                                , coluna_foco='CNPJ_FUNDO')



#%%
# --------------- 1ª AVALIAÇÃO GRÁFICA DE H2 ---------------
sns.displot(data=df_H2, x='DATA'
                        , y='RENTABILIDADE' 
                        , hue="PERIODO"
                        , linewidth=3
                        ,kind='hist'
                        )
sns.lineplot(data=df_H2, x='DATA'
                        , y='MEDIA' 
                        , color = 'black'
                        , linewidth=1
                        )
#sns.set(xlabel = '')


plt.title("Histograma da Rentabilidade dos fundos de ações no Brasil")
plt.xlabel("Meses Corridos (01/2017 à 12/2022)")
plt.ylabel("Rentabilidade (%)")

plt.axvline(0, color='black', linestyle='dotted' , linewidth=0.8)
plt.axvline(12, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(24, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(36, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(48, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(60, color='black', linestyle='dotted', linewidth=0.8)
plt.axvline(72, color='black', linestyle='dotted', linewidth=0.8)

plt.show()


#%%
# --------------- MÁXIMO E MÍNIMO DA MÉDIA DE RENTABILIDADE DO PERÍODO ---------------
h2_max_value = df_H2["MEDIA"].max()
h2_min_value = df_H2["MEDIA"].min()

# obtendo os índices dos valores máximos e mínimos da coluna MEDIA
h2_max_index = df_H2["MEDIA"].idxmax()
h2_min_index = df_H2["MEDIA"].idxmin()

# obtendo os valores da coluna MES correspondentes aos valores máximos e mínimos da coluna MEDIA
h2_max_month = df_H2.loc[h2_max_index, "DATA"]
h2_min_month = df_H2.loc[h2_min_index, "DATA"]


# %% 
# --------------- 2ª AVALIAÇÃO GRÁFICA DE H2 ---------------
resumo_H2_1 = df_H2.groupby('PERIODO').agg({'MEDIA':'mean'}).reset_index()
resumo_H2_1 = resumo_H2_1.iloc[[1, 0]]

sns.barplot(data=resumo_H2_1, x='PERIODO', y='MEDIA', hue='PERIODO')
plt.title("Média de rendimento/mês por Período")
plt.xlabel("Periodo")
plt.ylabel("Rendimento %")
plt.show()


# %%
# --------------- 3ª AVALIAÇÃO GRÁFICA DE H2 ---------------
resumo_H2_2 = df_H2[~df_H2['DATA'].isin(['2020-03', '2020-04', '2020-05'])]
resumo_H2_2 = resumo_H2_2.groupby('PERIODO').agg({'MEDIA':'mean'}).reset_index()
resumo_H2_2 = resumo_H2_2.iloc[[1, 0]]

sns.barplot(data=resumo_H2_2, x='PERIODO', y='MEDIA', hue='PERIODO')
plt.title("Média de rendimento/mês por Período")
plt.xlabel("Periodo")
plt.ylabel("Rendimento %")
plt.show()




# %%
# --------------- INICIANDO TRATAMENTO PARA VALIDAÇÃO DE H3 ---------------
# H3: A pandemia do COVID-19 afetou de forma diferente os fundos de ações 
# de acordo com a sua classificação Anbima, sendo que os fundos de ações livres 
# foram os mais afetados negativamente em termos de volume e rentabilidade.

# RESUMO VOLUME POR CLASSE ANBIMA
resumo_H3_vol = gera_base_volume(df_base=df_informes
                                 , columns_groupby=['MES', 'ANO', 'CLASSE_ANBIMA'])
resumo_H3_vol = resumo_H3_vol.droplevel(1, axis=1)

#RESUMO RENTABILIDADE POR CLASSE
resumo_H3_ren = gera_base_rentabilidade(
    df_base=df_informes
    , columns_groupby= ['CLASSE_ANBIMA', 'ANO', 'MES', 'CNPJ_FUNDO']
    ,coluna_foco= ['CLASSE_ANBIMA', 'CNPJ_FUNDO']
    )

temp = ['CLASSE_ANBIMA', 'ANO', 'MES', 'DATA', 'PERIODO']
resumo_H3_ren = resumo_H3_ren.groupby(temp).agg(
    {'RENTABILIDADE': 'mean'})

for i, v in enumerate(temp):
    resumo_H3_ren[v] = resumo_H3_ren.index.get_level_values(i)
resumo_H3_ren = resumo_H3_ren.reset_index(drop=True)



# %%
# --------------- 1ª AVALIAÇÃO GRÁFICA DE H3 - VOLUME ---------------
resumo_H3_vol = resumo_H3_vol.sort_values(by='DATA').reset_index(drop=True)

classes = resumo_H3_vol["CLASSE_ANBIMA"].unique() 

for classe in classes:
  df_classe = resumo_H3_vol[resumo_H3_vol["CLASSE_ANBIMA"] == classe]
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
  sns.lineplot(data=df_classe, x="DATA", y="VOLUME", hue="PERIODO", ax=ax1, palette="mako", style="PERIODO", markers=True)
  sns.boxplot(data=df_classe, x="PERIODO", y="VOLUME", ax=ax2, palette="mako", dodge=False, width=0.5, linewidth=2) 
  fig.suptitle(f"Volume de investimento por período para a classe {classe}")
  plt.show() # mostrar a figura


# %%
# --------------- GERANDO TABELA RESUMO DE H3 - VOLUME ---------------
resumo_H3_vol = resumo_H3_vol[['ANO', 'MES', 'PERIODO'
                               , 'CLASSE_ANBIMA', 'DATA', 'VOLUME']]

df_H3_vol = resumo_H3_vol.groupby(['CLASSE_ANBIMA', 'PERIODO']).agg({'VOLUME': 'sum'})

df_H3_vol['CLASSE_ANBIMA'] = df_H3_vol.index.get_level_values(0)
df_H3_vol['PERIODO'] = df_H3_vol.index.get_level_values(1)
df_H3_vol = df_H3_vol.reset_index(drop=True)

df_H3_vol = df_H3_vol[['CLASSE_ANBIMA', 'PERIODO', 'VOLUME']]


# %%
# --------------- 2ª AVALIAÇÃO GRÁFICA DE H3 - RENTABILIDADE ---------------
resumo_H3_ren = resumo_H3_ren.sort_values(by='DATA').reset_index(drop=True)
classes = resumo_H3_ren["CLASSE_ANBIMA"].unique() 

for classe in classes: 
    if classe == 'Ações Livre':
        df_classe = resumo_H3_ren[resumo_H3_ren["CLASSE_ANBIMA"] == classe] 
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) 
        sns.set_style("darkgrid") 
        sns.lineplot(data=df_classe, x="DATA", y="RENTABILIDADE", hue="PERIODO", ax=ax1, palette="rocket", style="PERIODO", markers=True) 
        sns.set_style("white") 
        sns.boxplot(data=df_classe, x="PERIODO", y="RENTABILIDADE", ax=ax2, palette="pastel", dodge=False, width=0.5, linewidth=2, notch=True) 
        fig.suptitle(f"Rentabilidade de investimento por período para a classe {classe}") 
        plt.show() 



# %%
# --------------- GERANDO TABELA RESUMO DE H3 - RENTABILIDADE ---------------
resumo_H3_ren = resumo_H3_ren[['ANO', 'MES', 'PERIODO'
                               , 'CLASSE_ANBIMA', 'DATA', 'RENTABILIDADE']]

df_H3_ren = resumo_H3_ren.groupby(['CLASSE_ANBIMA', 'PERIODO']).agg({'RENTABILIDADE': 'mean'})

df_H3_ren['CLASSE_ANBIMA'] = df_H3_ren.index.get_level_values(0)
df_H3_ren['PERIODO'] = df_H3_ren.index.get_level_values(1)
df_H3_ren = df_H3_ren.reset_index(drop=True)

df_H3_ren = df_H3_ren[['CLASSE_ANBIMA', 'PERIODO', 'RENTABILIDADE']]




# %%
# --------------- INICIANDO TRATAMENTO PARA VALIDAÇÃO DE H4 ---------------
# A pandemia do COVID-19 afetou de forma diferente os fundos de ações de acordo com 
# o seu perfil de risco, sendo que os fundos de ações de maior risco foram os mais 
# afetados negativamente em termos de volume e rentabilidade.

# RESUMO VOLUME POR CLASSE ANBIMA
resumo_H4_vol = gera_base_volume(df_base=df_informes
                                 , columns_groupby=['MES', 'ANO', 'PUBLICO_ALVO'])
resumo_H4_vol = resumo_H4_vol.droplevel(1, axis=1)


#RESUMO RENTABILIDADE POR CLASSE
resumo_H4_ren = gera_base_rentabilidade(
    df_base=df_informes
    , columns_groupby= ['PUBLICO_ALVO', 'ANO', 'MES', 'CNPJ_FUNDO']
    ,coluna_foco= ['PUBLICO_ALVO', 'CNPJ_FUNDO']
    )

temp = ['PUBLICO_ALVO', 'ANO', 'MES', 'DATA', 'PERIODO']
resumo_H4_ren = resumo_H4_ren.groupby(temp).agg(
    {'RENTABILIDADE': 'mean'})

for i, v in enumerate(temp):
    resumo_H4_ren[v] = resumo_H4_ren.index.get_level_values(i)
resumo_H4_ren = resumo_H4_ren.reset_index(drop=True)


# %%
# --------------- 1ª AVALIAÇÃO GRÁFICA DE H4 - VOLUME ---------------
resumo_H4_vol = resumo_H4_vol.sort_values(by='DATA').reset_index(drop=True)

pbc_alvo = resumo_H4_vol["PUBLICO_ALVO"].unique() 

for publico in pbc_alvo:
    df_publico_alvo = resumo_H4_vol[resumo_H4_vol["PUBLICO_ALVO"] == publico]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={"wspace": 0.3})
    sns.lineplot(data=df_publico_alvo, x="DATA", y="VOLUME", hue="PERIODO", ax=ax1, palette="flare", style="PERIODO", markers=["o", "s", "D", "*"])
    sns.boxplot(data=df_publico_alvo, x="PERIODO", y="VOLUME", ax=ax2, palette="rocket", dodge=False, width=0.5, linewidth=2) 
    fig.suptitle(f"Volume de investimento por período - Investidor {publico}", fontsize=16)
    plt.show() 


# %%
# --------------- GERANDO TABELA RESUMO DE H4 - VOLUME ---------------
resumo_H4_vol = resumo_H4_vol[['ANO', 'MES', 'PERIODO'
                               , 'PUBLICO_ALVO', 'DATA', 'VOLUME']]

df_H4_vol = resumo_H4_vol.groupby(['PUBLICO_ALVO', 'PERIODO']).agg({'VOLUME': 'sum'})

df_H4_vol['PUBLICO_ALVO'] = df_H4_vol.index.get_level_values(0)
df_H4_vol['PERIODO'] = df_H4_vol.index.get_level_values(1)
df_H4_vol = df_H4_vol.reset_index(drop=True)

df_H4_vol = df_H4_vol[['PUBLICO_ALVO', 'PERIODO', 'VOLUME']]


# %%
# --------------- 2ª AVALIAÇÃO GRÁFICA DE H4 - RENTABILIDADE ---------------
resumo_H4_ren = resumo_H4_ren.sort_values(by='DATA').reset_index(drop=True)
pbc_alvo = resumo_H4_ren["PUBLICO_ALVO"].unique() 

for publico in pbc_alvo: 
    df_publico_alvo = resumo_H4_ren[resumo_H4_ren["PUBLICO_ALVO"] == publico] 
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={"wspace": 0.3}) 
    sns.lineplot(data=df_publico_alvo, x="DATA", y="RENTABILIDADE", hue="PERIODO", ax=ax1, palette="mako", style="PERIODO", markers=True) 
    ax1.set_title("Rentabilidade por data", fontsize=14)
    sns.boxplot(data=df_publico_alvo, x="PERIODO", y="RENTABILIDADE", ax=ax2, palette="flare", dodge=False, width=0.5, linewidth=2, notch=True) 
    ax2.set_title("Rentabilidade por período", fontsize=14)
    fig.suptitle(f"Rentabilidade de investimento por período - Investidor {publico}", fontsize=16) 
    plt.show()


# %%
# --------------- GERANDO TABELA RESUMO DE H4 - RENTABILIDADE ---------------
resumo_H4_ren = resumo_H4_ren[['ANO', 'MES', 'PERIODO'
                               , 'PUBLICO_ALVO', 'DATA', 'RENTABILIDADE']]

df_H4_ren = resumo_H4_ren.groupby(['PUBLICO_ALVO', 'PERIODO']).agg({'RENTABILIDADE': 'mean'})

df_H4_ren['PUBLICO_ALVO'] = df_H4_ren.index.get_level_values(0)
df_H4_ren['PERIODO'] = df_H4_ren.index.get_level_values(1)
df_H4_ren = df_H4_ren.reset_index(drop=True)

df_H4_ren = df_H4_ren[['PUBLICO_ALVO', 'PERIODO', 'RENTABILIDADE']]




# %%
# --------------- INICIANDO TRATAMENTO PARA VALIDAÇÃO DE H5 ---------------
# A rentabilidade dos fundos de ações foi menor que o desempenho do índice Ibovespa 
# no período da pandemia do COVID-19.
#df_ibov_mes = ibov.copy()
#df_H5 = gera_base_rentabilidade(df_base=df_informes
#                                , columns_groupby=['CNPJ_FUNDO','ANO', 'MES']
#                                , coluna_foco='CNPJ_FUNDO')
#
#temp = ['ANO', 'MES', 'PERIODO', 'DATA']
#df_H5 = df_H5.groupby(['ANO', 'MES', 'PERIODO', 'DATA']).agg({'RENTABILIDADE': 'mean'})
#for i, v in enumerate(temp):
#    df_H5[v] = df_H5.index.get_level_values(i)
#df_H5 = df_H5.reset_index(drop=True)
#
## %%
#df_ibov_mes = ibov.copy()
#df_ibov_mes['MES'] = df_ibov_mes['DATA'].dt.strftime('%m')
#df_ibov_mes['MES'] = [int(x) for x in df_ibov_mes['MES']]
#df_ibov_mes['ANO'] = df_ibov_mes['DATA'].dt.strftime('%Y')
#df_ibov_mes['ANO'] = [int(x) for x in df_ibov_mes['ANO']]
#df_ibov_mes = pd.DataFrame(df_ibov_mes.groupby(['ANO', 'MES'])[
#    'IBOVESPA'].last().pct_change())
#
#temp = ['ANO', 'MES']
#for i, v in enumerate(temp):
#    df_ibov_mes[v] = df_ibov_mes.index.get_level_values(i)
#df_ibov_mes = df_ibov_mes.reset_index(drop=True)
#df_ibov_mes.dropna(subset=['IBOVESPA'], inplace=True)
#df_ibov_mes['IBOVESPA'] = df_ibov_mes['IBOVESPA']*100
#
#df_H5 = df_H5.merge(df_ibov_mes, how='inner', on=['ANO', 'MES'])
#df_H5['DATA'] = pd.to_datetime(df_H5['DATA'])
#
#
## %%
#sns.lineplot(data=df_H5
#            , x='DATA'
#            , y='RENTABILIDADE' 
#            #, hue="IBOVESPA"
#            , label='FI Ações'
#            , linewidth=1.5
#            , color = 'blue'
#            )
#
#sns.lineplot(data=df_H5
#            , x='DATA'
#            , y='IBOVESPA' 
#            #, hue="IBOVESPA"
#            , label='IBOVESPA'
#            , linewidth=1.5
#            , color = 'green'
#            )
#
#plt.legend()
#
#plt.title("Rentabilidade dos Fundos de Ações x IBOVESPA")
#plt.xlabel("Meses Corridos (01/2017 à 12/2022)")
#plt.ylabel("Rentabilidade (%)")
#
#plt.show()
#
#
##%%
#def gera_base_rentabilidade_2(df_base, columns_groupby:list, coluna_foco):
#    df_resultado = df_base.groupby(columns_groupby).agg({'VL_QUOTA': 'mean'})
#    df_resultado['RENTABILIDADE'] = df_resultado.groupby(coluna_foco)['VL_QUOTA'].pct_change()*100
#
#    for i, v in enumerate(columns_groupby):
#        df_resultado[v] = df_resultado.index.get_level_values(i)
#    df_resultado = df_resultado.reset_index(drop=True)
#
#    df_resultado.dropna(subset=['RENTABILIDADE'], inplace=True)
#
#    return df_resultado
#
#
#
## %%
#df_H5 = gera_base_rentabilidade_2(df_base=df_informes
#                                , columns_groupby=['CNPJ_FUNDO','ANO']
#                                , coluna_foco='CNPJ_FUNDO')
#
#temp = ['ANO']
#df_H5 = df_H5.groupby(['ANO']).agg({'RENTABILIDADE': 'mean'})
#for i, v in enumerate(temp):
#    df_H5[v] = df_H5.index.get_level_values(i)
#df_H5 = df_H5.reset_index(drop=True)
#
## %%
#df_ibov_mes = ibov.copy()
#
#df_ibov_mes['ANO'] = df_ibov_mes['DATA'].dt.strftime('%Y')
#df_ibov_mes['ANO'] = [int(x) for x in df_ibov_mes['ANO']]
#df_ibov_mes = pd.DataFrame(df_ibov_mes.groupby(['ANO'])[
#    'IBOVESPA'].last().pct_change())
#
#temp = ['ANO']
#for i, v in enumerate(temp):
#    df_ibov_mes[v] = df_ibov_mes.index.get_level_values(i)
#df_ibov_mes = df_ibov_mes.reset_index(drop=True)
#df_ibov_mes.dropna(subset=['IBOVESPA'], inplace=True)
#df_ibov_mes['IBOVESPA'] = df_ibov_mes['IBOVESPA']*100
#
#
##%%
#df_H5 = df_H5.merge(df_ibov_mes, how='inner', on=['ANO'])
#df_H5 = df_H5[['ANO', 'IBOVESPA','RENTABILIDADE']]
#
## %%
#