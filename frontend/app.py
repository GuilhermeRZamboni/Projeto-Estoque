import streamlit as st
import requests 
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Sistema de Gerenciamento de Estoque", layout="wide", page_icon="📦")
st.title("Sistema de Gerenciamento de Estoque")

menu = st.sidebar.radio("Menu", ["Todos Produtos","Adicionar Produto" , "Atualizar Produto", "Deletar Produto"])


