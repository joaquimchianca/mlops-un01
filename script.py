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

def run_script():
    '''Plota o gráfico feito durante o Projeto Guiado do DataQuest

        Args: None

        Retorna figure.
    '''
    try:
        exchange_rates = pd.read_csv('euro-daily-hist_1999_2020.csv')
    except FileNotFoundError:
        print("File not found.")
    except pd.errors.EmptyDataError:
        print("No data")
    except pd.errors.ParserError:
        print("Parse error")


    #Mudança do nome das colunas do DataFrame para melhorar o código
    exchange_rates.rename(columns={'[US dollar ]': 'US_dollar',
                                    'Period\\Unit:': 'Time',
                                    '[Brazilian real ]': 'BR_real'},
                          inplace=True)

    #Cast da coluna Time para o tipo Datetime
    exchange_rates['Time'] = pd.to_datetime(exchange_rates['Time'])

    exchange_rates.sort_values('Time', inplace=True) #ordenando os valores em ordem cronológica
    exchange_rates.reset_index(drop=True, inplace=True) #resetando o index do Dataframe

    #Criação do Dataframe utilizado no escopo do projeto contendo o valor em real e o tempo
    euro_to_real = exchange_rates[['Time', 'BR_real']].copy()

    #Limpeza do dataframe e casting da coluna BR_real para float
    euro_to_real = euro_to_real[euro_to_real['BR_real'] != '-']
    euro_to_real['BR_real'] = euro_to_real['BR_real'].astype(float)

    #Cria uma coluna com a cotação média por mês Euro/Real
    euro_to_real['rolling_mean'] = euro_to_real['BR_real'].rolling(30).mean()
    euro_to_real.tail()


    #Dataframe que referencia os anos pré pandemia (2016 a 2019)
    real_pre_corona = euro_to_real.copy(
                       )[(euro_to_real['Time'].dt.year >= 2016
                       ) & (euro_to_real['Time'].dt.year <= 2019)]

    #Dataframe que referencia os anos após o início da pandemia no Brasil (2020)
    real_corona = euro_to_real.copy()[euro_to_real['Time'].dt.year >= 2020]

    style.use('fivethirtyeight')

    #Plotando os graficos
    (fig, ax) = plt.subplots(figsize=(6.4,3))
    ax.plot(real_pre_corona['Time'], real_pre_corona['rolling_mean'], linewidth=2)
    ax.plot(real_corona['Time'], real_corona['rolling_mean'], color='#dc1515')
    ax.set_ylim([2.5,7])

    #Limpando o grafico
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(None)

    #Maximizando o data-ink ratio
    ax.text(y=1.8, x=18210,s='2020',color='grey')
    ax.text(y=4.2, x=18260, s='R$ 4,59')
    ax.text(y=5.9, x=18600, s='R$ 6,31')
    ax.text(y=3.7, x=16600, s='R$ 4,16')
    ax.text(y=6.2,x=18180, s='Corona', color='#dc1515', weight='bold')
    plt.plot(18265, 4.592367, marker='o', markersize=8, markerfacecolor='#5f5f5f', markeredgecolor='#5f5f5f')
    plt.plot(18620, 6.314330, marker='o', markersize=8, markerfacecolor='#5f5f5f', markeredgecolor='#5f5f5f')
    plt.plot(16800, 4.166533, marker='o', markersize=8, markerfacecolor='#5f5f5f', markeredgecolor='#5f5f5f')

    #Adicionando título e subtítulo
    ax.text(y=8, x=16450, size=14, weight='bold',
           s='Euro aumenta valor em 37,5% após 1 ano de pandemia')
    ax.text(y=7.6,x=16450,size=12,
           s='Cotação Euro/Real entre 2016 e 2021')

    #Adicionando rótulo
    ax.text(16450, 1.07, '©JOAQUIM' + ' '*92 + 'Fonte: Banco Central Europeu',
            color = '#f0f0f0', backgroundcolor = '#4d4d4d',
            size=10)
    return fig

def retrieve_code():
    '''Atribui o código do script a uma string

        Args: None

        Retorna string.
    '''
    return '''import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style

try:
    exchange_rates = pd.read_csv('euro-daily-hist_1999_2020.csv')
except FileNotFoundError:
    print("File not found.")
except pd.errors.EmptyDataError:
    print("No data")
except pd.errors.ParserError:
    print("Parse error")


#Mudança do nome das colunas do DataFrame para melhorar o código
exchange_rates.rename(columns={'[US dollar ]': 'US_dollar',
                                'Period\\Unit:': 'Time',
                                '[Brazilian real ]': 'BR_real'},
                      inplace=True)

#Cast da coluna Time para o tipo Datetime
exchange_rates['Time'] = pd.to_datetime(exchange_rates['Time'])

exchange_rates.sort_values('Time', inplace=True) #ordenando os valores em ordem cronológica
exchange_rates.reset_index(drop=True, inplace=True) #resetando o index do Dataframe

#Criação do Dataframe utilizado no escopo do projeto contendo o valor em real e o tempo
euro_to_real = exchange_rates[['Time', 'BR_real']].copy()

#Limpeza do dataframe e casting da coluna BR_real para float
euro_to_real = euro_to_real[euro_to_real['BR_real'] != '-']
euro_to_real['BR_real'] = euro_to_real['BR_real'].astype(float)

#Cria uma coluna com a cotação média por mês Euro/Real
euro_to_real['rolling_mean'] = euro_to_real['BR_real'].rolling(30).mean()
euro_to_real.tail()


#Dataframe que referencia os anos pré pandemia (2016 a 2019)
real_pre_corona = euro_to_real.copy(
                   )[(euro_to_real['Time'].dt.year >= 2016
                   ) & (euro_to_real['Time'].dt.year <= 2019)]

#Dataframe que referencia os anos após o início da pandemia no Brasil (2020)
real_corona = euro_to_real.copy()[euro_to_real['Time'].dt.year >= 2020]

style.use('fivethirtyeight')

#Plotando os graficos
(fig, ax) = plt.subplots(figsize=(6.4,3))
ax.plot(real_pre_corona['Time'], real_pre_corona['rolling_mean'], linewidth=2)
ax.plot(real_corona['Time'], real_corona['rolling_mean'], color='#dc1515')
ax.set_ylim([2.5,7])

#Limpando o grafico
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(None)

#Maximizando o data-ink ratio
ax.text(y=1.8, x=18210,s='2020',color='grey')
ax.text(y=4.2, x=18260, s='R$ 4,59')
ax.text(y=5.9, x=18600, s='R$ 6,31')
ax.text(y=3.7, x=16600, s='R$ 4,16')
ax.text(y=6.2,x=18180, s='Corona', color='#dc1515', weight='bold')
plt.plot(18265, 4.592367, marker='o', markersize=8, markerfacecolor='#5f5f5f', markeredgecolor='#5f5f5f')
plt.plot(18620, 6.314330, marker='o', markersize=8, markerfacecolor='#5f5f5f', markeredgecolor='#5f5f5f')
plt.plot(16800, 4.166533, marker='o', markersize=8, markerfacecolor='#5f5f5f', markeredgecolor='#5f5f5f')

#Adicionando título e subtítulo
ax.text(y=8, x=16450, size=14, weight='bold',
       s='Euro aumenta valor em 37,5% após 1 ano de pandemia')
ax.text(y=7.6,x=16450,size=12,
       s='Cotação Euro/Real entre 2016 e 2021')

#Adicionando rótulo
ax.text(16450, 1.07, '©JOAQUIM' + ' '*92 + 'Fonte: Banco Central Europeu',
        color = '#f0f0f0', backgroundcolor = '#4d4d4d',
        size=10)'''