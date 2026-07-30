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
