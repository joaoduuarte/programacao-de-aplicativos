import sqlite3

def cadastrar_professor(nome,cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # o sistema aceita cadastrar dois professores com o mesmo CPF.
    #como restringir isso direto na estrutura da tabela abaixo?
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores ( 
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT
        )
    ''')
#Se a tabela já existe
#CREATE TABLE IF NOT EXISTS não altera uma tabela existente. Se você já criou a tabela sem UNIQUE, a restrição não será adicionada automaticamente.

import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE
        )
    """)

    try:
                cursor.execute("""
            INSERT INTO professores (nome, cpf)
            VALUES (?, ?)
        """, (nome, cpf))

        conexao.commit()
        print("Professor cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: já existe um professor com esse CPF!")

    finally:
        conexao.close()


cadastrar_professor("João Silva", "123.456.789-00")
cadastrar_professor("Maria Souza", "987.654.321-00")
cadastrar_professor("Pedro Santos", "123.456.789-00")  # CPF repetido