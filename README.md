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
Configure `.env` com:
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT

## Como rodar
1. Rodar o backend (na raiz do projeto):
```sh
uvicorn backend.api:app --reload --host 127.0.0.1 --port 8000
```
2. Rodar o frontend (em outro terminal):
```sh
streamlit run h:\Projeto Estoque\frontend\app.py
```

## Endpoints principais (FastAPI)
- GET / — saudação
- GET /produtos — listar produtos
- POST /produtos — adicionar produto (params: nome, categoria, preco, quantidade)
- PUT /produtos/{id} — atualizar produto (params: preco, quantidade)
- DELETE /produtos/{id} — deletar produto

## Exemplos (curl)
Adicionar:
```sh
curl -X POST "http://127.0.0.1:8000/produtos?nome=Mouse&categoria=Eletronicos&preco=220&quantidade=25"
```
Listar:
```sh
curl "http://127.0.0.1:8000/produtos"
```

---