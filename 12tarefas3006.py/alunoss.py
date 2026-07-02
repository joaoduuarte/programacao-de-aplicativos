import sqlite3

def autualizar_nome_aluno(id_aluno,novo_nome):
    conexao = sqlite3.connect ('sistema_escola.db')
    cursor = conexao.cursor()

    #o professor pediu para mudar o nome do aluno de id 3,
    # mas o sistema alterou o nome de todos os alunos do banco de dados! correção
    # urgente :

    cursor.execute("UPDATE alunos SET nome = ?", (novo_nome))

    conexao.commit()
    conexao.close()

#O problema é que o comando UPDATE está sem a cláusula WHERE. Sem ela, o SQLite atualiza todas as linhas da tabela.

import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE alunos SET nome = ? WHERE id = ?",
        (novo_nome, id_aluno)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Nome do aluno atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")

    conexao.close()