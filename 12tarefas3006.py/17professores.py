import sqlite3

def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
    	# Existe um erro de digitação no comando SQL (INSERTO).  
    	# Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe? 
        cursor.execute("INSERTO INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 
    except sqlite3.Error: 
        print("Erro: Este CPF já está cadastrado no sistema!") 
    finally: 
        conexao.close() 

# codigo certo

import sqlite3


def inserir_professor(nome, materia, cpf):
    conexao = None

    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        # Existe um erro de digitação no comando SQL (INSERTO).
        # Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe?

        cursor.execute(
            "INSERT INTO professores (nome, materia, cpf) VALUES (?, ?, ?)",
            (nome, materia, cpf)
        )

        conexao.commit()

    except sqlite3.IntegrityError:
        print("Erro: Este CPF já está cadastrado no sistema.")

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)

    finally:
        if conexao:
            conexao.close()

# O erro acontecia porque `sqlite3.Error` capturava qualquer falha do SQLite e exibia uma mensagem incorreta de CPF duplicado,
#  mesmo quando o problema era a sintaxe do SQL (`INSERTO` em vez de `INSERT`).
#  A correção foi separar os tratamentos de erro, usando `sqlite3.IntegrityError`
#  para problemas como CPF duplicado e `sqlite3.Error` para outros erros do banco.
# S Também foi protegido o fechamento da conexão no `finally` para evitar novos erros caso ela não tenha sido criada.


