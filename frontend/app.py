import streamlit as st
import requests 
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Sistema de Gerenciamento de Estoque", layout="wide", page_icon="📦")
st.title("Sistema de Gerenciamento de Estoque")

menu = st.sidebar.radio("Menu", ["Todos Produtos","Adicionar Produto" , "Atualizar Produto", "Deletar Produto"])


if menu == "Todos Produtos":
    st.header("Lista de Produtos")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        st.dataframe(produtos)
    else:
        st.error("Erro ao buscar produtos")
