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

