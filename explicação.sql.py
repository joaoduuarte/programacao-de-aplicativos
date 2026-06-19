import sqlite3

# Conecta ao banco de dados de teste
conexao = sqlite3.connect("aula_comandos.db")
cursor = conexao.cursor()

print("1. Executando: CREATE TABLE...")
# Criando a tabela do zero
cursor.execute('''
    CREATE TABLE IF NOT EXISTS professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        materia TEXT,
        id_aluno INTEGER,
        FOREIGN KEY (id_aluno) REFERENCES alunos(id)
    )
''')


conexao.commit()

print("2. Executando: INSERT INTO...")
# Inserindo dois registros de teste
cursor.execute("INSERT INTO professores (nome, materia) VALUES ('Allan', 'Python');")
cursor.execute("INSERT INTO professores (nome, materia) VALUES ('Marcos', 'Geografia');")
conexao.commit()

print("3. Executando: UPDATE...")
# Alterando a matéria do professor Allan (ID 1)
cursor.execute("UPDATE professores SET materia = 'Banco de Dados' WHERE id = 1;")
conexao.commit()

print("4. Executando: ALTER TABLE...")
# Adicionando uma coluna nova que não existia na criação
try:
    cursor.execute("ALTER TABLE professores ADD COLUMN telefone TEXT;")
    conexao.commit()
    print("   -> Coluna 'telefone' adicionada com sucesso!")
except sqlite3.OperationalError:
    print("   -> A coluna 'telefone' já tinha sido adicionada antes.")

# Mostrando o resultado atual na tela antes do comando final
cursor.execute("SELECT * FROM professores;")
professores = cursor.fetchall()
print("\n--- Dados atuais no Banco ---")
for linha in professores:
    print(linha)

print("\n5. Executando: DROP TABLE...")
# Apagando a tabela inteira para deixar o banco limpo para o próximo teste
cursor.execute("DROP TABLE professores;")
conexao.commit()
print("   -> Tabela excluída com sucesso!")

# Fecha o banco
conexao.close()