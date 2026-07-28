import sqlite3 
 
def vincular_aluno_turma(): 
	nome = input("Nome do aluno: ") 
	# Se o usuário digitar "Turma B" em vez do número do ID, o sistema quebra. 
	# O try/except abaixo falhou em capturar esse erro. Qual o problema? 

import sqlite3

def vincular_aluno_turma():
    try:
        nome = input("Nome do aluno: ")
        turma_id = int(input("ID da turma: "))

        conn = sqlite3.connect("escola.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO aluno_turma (nome_aluno, turma_id) VALUES (?, ?)",
            (nome, turma_id)
        )

        conn.commit()
        print("Aluno vinculado à turma com sucesso!")

    except ValueError:
        print("Erro: o ID da turma deve ser um número inteiro.")

    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

    finally:
        try:
            conn.close()
        except NameError:
            pass

vincular_aluno_turma()

#Como "Turma B" não pode ser convertido para um número inteiro, o Python gera um ValueError. 
# Mas esse erro acontece antes de entrar no try, então o except nunca é executado e o programa encerra com uma mensagem de erro.
