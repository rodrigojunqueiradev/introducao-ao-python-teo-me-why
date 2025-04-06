import streamlit as st
import requests
import pandas as pd

URL = "https://viacep.com.br/ws/{cep}/json/"

st.title("Busca CEP")

cep = st.text_input("Informe o CEP:")

if cep != "":

    try:
        resp = requests.get(URL.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data, hide_index=True)

    except Exception as err:
        st.error("Entre com um CEP válido!")