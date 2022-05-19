import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import script


header = st.container()
body = st.container()
code = st.container()

script2 = script.retrieve_code()

fig = script.run_script()
with header:
    st.title("Trabalho Final MLOps Unidade 1")
    st.text('Dashboard contendo solução do trabalho.')
    st.text('Feito por Joaquim Chianca')

with body:
    st.header('Plot')
    st.write(fig)


with code:
    st.header('Code')
    st.code(script2, language='python')