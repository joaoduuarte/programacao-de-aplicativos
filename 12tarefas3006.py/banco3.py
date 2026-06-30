import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #este bloco quebra ao rodar pela primeira vez em um banco limpo. por que?
    cursor.execute(''' CREATE TABLE IF NOT EXISTS series ( 
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_serie TEXT,
                   id_esocola INTEGER,
                   FOREIGN KEY ( id_escola) REFERENCES escolas (id)  )
                   ''')
    
    cursor.execute('''  CREATE TABLE IF NOT EXIST escolas (
                id INTERGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT
               )
               ''')
    conexao.commit()
    conexao.close()

# Em um banco novo, o Python executa o código de cima para baixo.
# Como a tabela `series` é criada antes da tabela `escolas`, a chave estrangeira tenta apontar para uma tabela que ainda não existe,
#  o que pode causar erro. Por isso, o ideal é criar primeiro a tabela `escolas` e depois a tabela `series`.


print("=== codigo certo ====")

import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS escolas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT
                   ) ''')
    
    cursor.execute(''' CREATE TABLE IF NOT EXISTS series ( 
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome_serie TEXT,
                   id_escola INTEGER,
                   FOREIGN KEY (id_escola) REFERENCES escolas (id)
                   ) ''')
    
    conexao.commit()
    conexao.close()

criar_tabelas()
