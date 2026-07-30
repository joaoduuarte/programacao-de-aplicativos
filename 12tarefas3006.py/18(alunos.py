import sqlite3 

def cadastrar_lista_alunos(): 
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)] 
     
conexao = sqlite3.connect('sistema_escola.db') 
cursor = conexao.cursor() 
     
	# O comando executemany quebra com a mensagem: "function takes exactly 2 arguments". 
	# Como passar a lista de dados da forma correta dentro dele? 
cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", ) 
     
conexao.commit() 
conexao.close() 

#codigo certo

import sqlite3


def cadastrar_lista_alunos():
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)]

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O comando executemany quebra com a mensagem:
    # "function takes exactly 2 arguments".
    # Como passar a lista de dados da forma correta dentro dele?

    cursor.executemany(
        "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
        lista
    )

    conexao.commit()
    conexao.close()

# O problema principal era que o código utilizava cursor.execute() para inserir uma lista de vários registros.
#  O método execute() é usado para executar um único comando por vez,
#  enquanto o executemany() deve ser utilizado quando queremos inserir vários dados de uma vez.
