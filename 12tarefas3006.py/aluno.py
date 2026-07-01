import sqlite3

def vincular_aluno_turma():
    nome = input ("nome do aluno : ")
    #se o usuario digitar " turma B" em vez do numero do id< o sistema quebra.
    # o try/ except abaixo falhou em capturar esse erro. qual o problema?
    try :
        id_turma = int(input("digite o id numerico da truma: "))

        conexao = sqlite3.connect(' sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALEUS (?, ?)", (nome, id_turma))
        conexao.commit()
    except sqlite3. error: 
        print("error no bamco de dados!")
    finally: 
        conexao.close()

# O erro acontece porque o Python tenta converter um texto em número usando `int()`.
#  Como isso gera um `ValueError` (erro do Python), e não um `sqlite3.Error` (erro do banco de dados), 
# ele não é tratado pelo `except sqlite3.Error`.

print("==== codigo certo =====")

import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    conexao = None

    try:
                id_turma = int(input("Digite o ID numérico da turma: "))

                conexao = sqlite3.connect("sistema_escola.db")
        cursor = conexao.cursor()

                cursor.execute(
            "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
            (nome, id_turma)
        )

        conexao.commit()
        print("Aluno vinculado à turma com sucesso!")

    except ValueError:
        print("Erro: o ID da turma deve ser um número inteiro.")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")

    finally:
        if conexao is not None:
            conexao.close()

vincular_aluno_turma()
