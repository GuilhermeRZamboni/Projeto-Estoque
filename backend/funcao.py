from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                categoria VARCHAR(50),
                preco NUMERIC,
                quantidade INT);""")
            conexao.commit()

        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()
# criar_tabela()


def adicionar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""INSERT INTO produtos (nome, categoria, preco, quantidade)
                              VALUES (%s, %s, %s, %s);""",
                           (nome, categoria, preco, quantidade))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao adicionar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

# adicionar_produto("Mouse", "Eletrônicos", 220, 25)

def listar_produtos(): 
    conexao, cursor = conectar()
    produtos = []
    if conexao:
        try:
            cursor.execute("SELECT * FROM produtos ORDER BY id;")
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar produtos: {erro}")
        finally:
            cursor.close()
            conexao.close()

print(listar_produtos())

def atualizar_produto(id, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            if preco != -1:
                if quantidade != -1:
                    cursor.execute("""UPDATE produtos
                                    SET preco = %s, quantidade = %s
                                    WHERE id = %s;""",
                                (preco, quantidade, id))
                else:
                    cursor.execute("""UPDATE produtos
                                    SET preco = %s 
                                    WHERE id = %s;""",
                                (preco, id))
            else:
                if quantidade != -1:
                    cursor.execute("""UPDATE produtos
                                    SET quantidade = %s
                                    WHERE id = %s;""",
                                (quantidade, id))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()
# atualizar_produto(2, 100.00, 10)
def deletar_produto(id):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("DELETE FROM produtos WHERE id = %s;", (id,))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar produto: {erro}")
        finally:
            cursor.close()
            conexao.close()
