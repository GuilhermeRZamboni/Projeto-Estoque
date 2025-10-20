from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de Filmes")

@app.get("/")
