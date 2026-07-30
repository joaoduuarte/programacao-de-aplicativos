import sqlite3


def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    # O SQLite joga um erro de sintaxe operacional indicando que não aceita o caractere '?'.
    # Não podemos parametrizar nomes de tabelas? Como resolver mantendo a segurança?
    cursor.execute(
        "SELECT * FROM ? WHERE id = ?",
        (nome_tabela, id_registro)
    )

    print(cursor.fetchone())
    conexao.close()

# codigo certo

import sqlite3


def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    # O SQLite não permite usar '?' para nomes de tabelas.
    # O nome da tabela deve ser validado antes de ser inserido na consulta.

    tabelas_permitidas = ["alunos", "professores", "turmas"]

    if nome_tabela not in tabelas_permitidas:
        print("Erro: tabela não permitida.")
        conexao.close()
        return

    cursor.execute(
        f"SELECT * FROM {nome_tabela} WHERE id = ?",
        (id_registro,)
    )

    print(cursor.fetchone())
    conexao.close()

# O erro ocorria porque o `?` só pode ser usado para substituir valores, não nomes de tabelas ou colunas.
#  A correção foi inserir o nome da tabela no comando SQL após validar se ele é permitido,
#  evitando problemas de segurança como injeção de SQL.

