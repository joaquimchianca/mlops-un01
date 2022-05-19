# Trabalho final Unidade 1
Este repositório armazena as soluções solicitadas no trabalho final da primeira unidade da disciplina MLOps.
Contém:
- Um arquivo com o script o qual plota o gráfico desejado (script.py);
- O arquivo que executa a aplicação em dashboard no Streamlit.io (app.py);
- Arquivo do dataset (euro-daily-hist_1999_2020.csv);
- Arquivo yml que contém as bibliotecas que podem ser usadas no Streamlit (environment.yml)

## Linha de raciocínio do projeto
[Texto no Medium](https://medium.com/@joaquimchianca/gr%C3%A1fico-valoriza%C3%A7%C3%A3o-assustadora-do-euro-em-um-ano-de-pandemia-fb331c859c42)

## Streamlit
Caso queira rodar o Streamlit localmente, execute a seguinte linha de comando

    $ streamlit run app.py

Se não tiver instalado o Streamlit, é necessário criar um novo ambiente usando o Conda

    $ conda env create streamlit //criação do novo ambiente
    $ conda activate [nome do ambiente] //ativa e muda para o novo ambiente
    $ pip install streamlit
    $ streamlit hello

