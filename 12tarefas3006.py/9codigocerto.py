import sqlite3


def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O professor pediu para mudar o nome do aluno de id 3,
    # mas o sistema alterou o nome de todos os alunos do banco de dados.
    # Correção urgente:

    cursor.execute(
        "UPDATE alunos SET nome = ? WHERE id = ?",
        (novo_nome, id_aluno)
    )

    conexao.commit()
    conexao.close()

#O problema principal era que o comando UPDATE não possuía uma condição WHERE. Quando um UPDATE é executado sem WHERE,
# o banco de dados aplica a alteração em todos os registros da tabela.