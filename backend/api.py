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

@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produtos()
    lista = []
    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome": produto[1],
            "categoria": produto[2],
            "preco": produto[3],
            "quantidade": produto[4]
        })
    return {"produtos": lista}

@app.put("/produtos/{produto_id}") 
def atualizar_produto(produto_id: int, preco: float, quantidade: int):
    funcao.atualizar_produto(produto_id, preco, quantidade)
    return {"mensagem": "Produto atualizado com sucesso!"}

@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int):
    funcao.deletar_produto(produto_id)
    return {"mensagem": "Produto deletado com sucesso!"}






