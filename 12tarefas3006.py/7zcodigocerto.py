import sqlite3


def cadastrar_turma(nome, id_series, id_prof):

    conexao = sqlite3.connect('sistema_escolas.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    try:
        cursor.execute(
            "INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)",
            (nome, id_series, id_prof)
        )

        conexao.commit()

    except sqlite3.IntegrityError:
        print("Erro: professor ou série informada não existe.")

    finally:
        conexao.close()
        
#O código apresentava vários problemas de escrita e estrutura.
#  Primeiro, havia erros de digitação, como onexao em vez de conexao, cursosr e curssr em vez de cursor, e VALEUS em vez de VALUES.
#  Também havia uma diferença entre os nomes dos parâmetros da função e os valores usados no comando SQL,
#  o que poderia causar erro na execução.
#O principal problema era a falta de tratamento de exceções. Caso o id_prof informado não existisse,
#  o SQLite geraria um IntegrityError por causa da chave estrangeira. Sem um bloco try/except/finally,
#  o programa seria interrompido antes de chegar ao conexao.close(), deixando a conexão aberta.
#Com o uso do finally, o fechamento da conexão acontece sempre, mesmo quando ocorre um erro.
#  Isso garante que os recursos do banco de dados sejam liberados corretamente.