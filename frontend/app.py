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
elif menu == "Adicionar Produto":
    st.header("Adicionar Novo Produto")
    nome = st.text_input("Nome do Produto")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade", min_value=0)
    if st.button("Adicionar Produto"):
        dados = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        }
        response= requests.post(f"{API_URL}/produtos", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar produto")

