import sqlite3

conexao = sqlite3.connect("sistema_escola.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS escolas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

conexao.commit()
conexao.close()

print("Tabela criada com sucesso!")

#O código apresenta alguns problemas. Primeiro, falta o `commit()`,
# que é responsável por confirmar e salvar as alterações realizadas no banco de dados.
# Também não há o `close()`, que deve ser utilizado para encerrar a conexão e liberar os recursos.
# Além disso, o comentário informando que "não tem banco de dados" está incorreto,
# pois o SQLite cria automaticamente o arquivo do banco quando a conexão é estabelecida com `sqlite3.connect()`.
# Por fim, os comentários contêm erros de escrita, como **"temabem"**, que deve ser **"também"**, e **"nao"**,
# que deve ser **"não"**, sendo recomendável escrever os comentários com letra maiúscula e pontuação para melhorar a legibilidade.
