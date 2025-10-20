from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de Produtos")

@app.get("/")

def saudacao():
    return {"mensagem": "Bem-vindo ao gerenciador de Produtos!"}

@app.post("/produtos")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.adicionar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!"}




