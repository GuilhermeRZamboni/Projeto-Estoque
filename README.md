# Projeto Estoque

Sistema simples de gerenciamento de estoque com backend em FastAPI e frontend em Streamlit.

## Estrutura
- backend/
  - api.py
  - conexao.py
  - funcao.py
- frontend/
  - app.py
- .env (variáveis de conexão com o banco)
- requirements.txt

## Requisitos
Instale dependências:
```sh
pip install -r requirements.txt
```

## Como rodar
1. Rodar o backend (na raiz do projeto):
```sh
cd backend
python -m uvicorn api:app --reload
```
2. Rodar o frontend (em outro terminal):
```sh
cd frontend
streamlit run app.py
```

## Endpoints principais (FastAPI)
- GET / — saudação
- GET /produtos — listar produtos
- POST /produtos — adicionar produto (params: nome, categoria, preco, quantidade)
- PUT /produtos/{id} — atualizar produto (params: preco, quantidade)
- DELETE /produtos/{id} — deletar produto

## Clone este repositório

```bash
git clone https://github.com/GuilhermeRZamboni/Projeto-Estoque
```
---