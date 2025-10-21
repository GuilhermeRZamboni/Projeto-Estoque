import streamlit as st
import requests 
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Sistema de Gerenciamento de Estoque", layout="wide", page_icon="📦")
st.title("Sistema de Gerenciamento de Estoque")

menu = st.sidebar.radio("Menu", ["Todos Produtos","Adicionar Produto" , "Atualizar Produto", "Deletar Produto"])

response = requests.get(f"{API_URL}/produtos")
if response.status_code == 200:
    dados = response.json().get("produtos", [])
    ids = [item['id'] for item in dados]
else:
    st.error("Erro ao buscar IDs dos produtos")

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

elif menu == "Atualizar Produto":
    st.header("Atualizar Produto")
    id = st.selectbox("Selecione o ID do Produto", ids)
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        produto_selecionado = next((item for item in produtos if item["id"] == id), None)
        if produto_selecionado:
            st.dataframe([produto_selecionado])
    else:
        st.error("Erro ao buscar detalhes do produto")
    preco = st.number_input("Novo Preço (-1 para não alterar)", value=-1.0, format="%.2f")
    quantidade = st.number_input("Nova Quantidade (-1 para não alterar)", value=-1)
    if st.button("Atualizar Produto"):
        dados = {
            "preco": preco,
            "quantidade": quantidade
        }
        response = requests.put(f"{API_URL}/produtos/{id}", params=dados)
        if response.status_code == 200:
            st.success("Produto atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar produto")

elif menu == "Deletar Produto":
    st.header("Deletar Produto")
    id = st.selectbox("Selecione o ID do Produto", ids)
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        produto_selecionado = next((item for item in produtos if item["id"] == id), None)
        if produto_selecionado:
            st.dataframe([produto_selecionado])
    else:
        st.error("Erro ao buscar detalhes do produto")
    if st.button("Deletar Produto"):
        response = requests.delete(f"{API_URL}/produtos/{id}")
        if response.status_code == 200:
            st.success("Produto deletado com sucesso!")
        else:
            st.error("Erro ao deletar produto")