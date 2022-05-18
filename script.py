#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Nesse projeto feito em jupyter notebook, vamos "plotar" um gráfico a fim de entender
o comportamento da moeda brasileira, o Real, em relação ao Euro.
Vamos entender tal comportamento ao visualizar um gráfico mostrando a cotação do Euro em reais
ao longo dos anos 2016-2019 (pré pandemia) e os anos 2020-2021 (pandemia).
O Euro é a moeda dos países da União Europeia e a fonte dos dados é o Banco Central Europeu.
O dataset foi criado por Daria Chemkaeva e está disponibilizado em:
https://www.kaggle.com/lsind18/euro-exchange-daily-rates-19992020
'''
#Leitura do dataset em .csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
#%matplotlib inline
#Se rodar no Jupyter Notebook, descomente a linha acima

try:
       exchange_rates = pd.read_csv('euro-daily-hist_1999_2020.csv')
except FileNotFoundError:
       print("File not found.")
except pd.errors.EmptyDataError:
       print("No data")
except pd.errors.ParserError:
       print("Parse error")
except Exception:
       print("Some other exception.")

# In[2]:


exchange_rates.info()


# In[3]:


#Mudança do nome das colunas do DataFrame para melhorar o código
exchange_rates.rename(columns={'[US dollar ]': 'US_dollar',
                                'Period\\Unit:': 'Time',
                                '[Brazilian real ]': 'BR_real'},
                      inplace=True)

#casting da coluna Time para o tipo Datetime
exchange_rates['Time'] = pd.to_datetime(exchange_rates['Time'])
exchange_rates.sort_values('Time', inplace=True) #ordenando os valores em ordem cronológica
exchange_rates.reset_index(drop=True, inplace=True) #resetando o index do Dataframe


# In[4]:


euro_to_real = exchange_rates[['Time', 'BR_real']].copy()
#criação do Dataframe utilizado no escopo do projeto contendo o valor em real e o tempo


# In[5]:


euro_to_real['BR_real'].value_counts()
#verifica se há valores que não são numeros


# In[6]:


euro_to_real = euro_to_real[euro_to_real['BR_real'] != '-']
euro_to_real['BR_real'] = euro_to_real['BR_real'].astype(float)
#limpeza dos '-' e cast para float dos valores da coluna BR_real do nosso dataframe


# In[7]:


#visualização do dataframe
plt.plot(euro_to_real['Time'], euro_to_real['BR_real'])
plt.xlabel("Tempo em anos")
plt.ylabel("Valor do euro em reais")
plt.show()


# In[8]:


#criação de uma coluna com a cotação média por mês

euro_to_real['rolling_mean'] = euro_to_real['BR_real'].rolling(30).mean()
euro_to_real.tail()


# In[134]:




#dataframe que referencia os anos pré pandemia (2016 a 2019)
real_pre_corona = euro_to_real.copy(
                   )[(euro_to_real['Time'].dt.year >= 2016
                   ) & (euro_to_real['Time'].dt.year <= 2019)]

#dataframe que referencia os anos após o início da pandemia no Brasil (2020)
real_corona = euro_to_real.copy()[euro_to_real['Time'].dt.year >= 2020]

style.use('fivethirtyeight')

#plotando os graficos
(fig, ax) = plt.subplots(figsize=(7,3))
ax.plot(real_pre_corona['Time'], real_pre_corona['rolling_mean'], linewidth=2)
ax.plot(real_corona['Time'], real_corona['rolling_mean'], color='#dc1515')
ax.set_ylim([2.5,7])

#limpando o grafico
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(None)

#adicionando ticks
ax.text(y=3.93,x=16450,s='R$ 4,00',  size=10, weight='bold', color='grey')
ax.text(y=6.9, x=16450,s='R$ 7,00', size=10, color='grey')
ax.text(y=2.9, x=16450,s='R$ 3,00', size=10, color='grey')
ax.text(y=1.8, x=16730,s='2016',color='grey')
ax.text(y=1.8, x=18210,s='2020',color='grey')
ax.text(y=1.8, x=18600,s='2021',color='grey')

#adicionando recursos visuais para aumentar foco na informação que quero entregar
ax.axhline(y=4, color='#e70cd7', linewidth=1)
ax.text(y=4.2, x=18260, s='R$ 4,59')
ax.text(y=5.9, x=18600, s='R$ 6,31')
ax.text(y=6.2,x=18180, s='Corona', color='#dc1515', weight='bold')
plt.plot(18265, 4.592367, marker='o', markersize=8,
       markerfacecolor='#5f5f5f', markeredgecolor='#5f5f5f')
plt.plot(18620, 6.314330, marker='o', markersize=8,
       markerfacecolor='#5f5f5f', markeredgecolor='#5f5f5f')

#Adicionando título e subtítulo
ax.text(y=8, x=16450, size=14, weight='bold',
       s='Euro aumenta valor em 37% após 1 ano de pandemia')
ax.text(y=7.6,x=16450,size=12,
       s='Cotação Euro/Real entre 2016 e 2021')

#Adicionando rótulo
ax.text(16450, 1.07, '©JOAQUIM' + ' '*105 + 'Fonte: Banco Central Europeu',
        color = '#f0f0f0', backgroundcolor = '#4d4d4d',
        size=10)

plt.show()
