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

