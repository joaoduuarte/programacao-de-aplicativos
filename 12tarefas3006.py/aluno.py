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
