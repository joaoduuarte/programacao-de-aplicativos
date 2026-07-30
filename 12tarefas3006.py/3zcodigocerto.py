import sqlite3


def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_serie TEXT,
            id_escola INTEGER,
            FOREIGN KEY (id_escola) REFERENCES escolas(id)
        )
    ''')

    conexao.commit()
    conexao.close()

# O código apresentava alguns erros de escrita e estrutura. A tabela `series` estava sendo criada antes da tabela `escolas`,
#  causando problema em um banco limpo, pois a chave estrangeira faz referência a uma tabela que ainda não existe.
#  Também havia erros de digitação, como `id_esocola` em vez de `id_escola`, `CREATE TABLE IF NOT EXIST`
#  em vez de `CREATE TABLE IF NOT EXISTS` e `INTERGER` em vez de `INTEGER`. Além disso,
#  faltavam ajustes na organização do comando SQL e no fechamento correto das instruções.
#Para evitar problemas com a chave estrangeira, a tabela `escolas`
# deve ser criada primeiro e a verificação de chaves estrangeiras deve ser ativada no SQLite.
