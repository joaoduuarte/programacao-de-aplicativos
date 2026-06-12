import sqlite3

arquivo = sqlite3.connect('cadastro_alunos.py ')
cursor = arquivo.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
    )
''')

nome_completo = (input("digite seu nome : "))
telefone = float(input("qual seu telefone :"))
turma = float(input("digite sua turma"))
idade = float(input("digite sua idade"))
cpf = float(input("digite seu cpf"))

comando_inserir = f'''
    INSERT INTO alunos (nome, telefone, turma, idade, cpf)
    VALUES ('{nome_completo}', '{telefone}', '{turma}', {idade}, '{cpf}')
'''
cursor.execute(comando_inserir)
arquivo.commit()

import sqlite3

# 1. Conexão com o banco de dados
conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

# 2. Comando SQL para buscar todos os alunos
comando_selecao = "SELECT * FROM Alunos;"

# 3. Execução do comando
cursor.execute(comando_selecao)

# 4. Recuperação dos dados (fetchall traz todas as linhas encontradas)
linhas = cursor.fetchall()

# 5. Exibição dos resultados no terminal
print("\n--- LISTA DE ALUNOS CADASTRADOS ---")
for linha in linhas:
    print(f"ID: {linha[0]} | Nome: {linha[1]} | Telefone: {linha[2]} | Turma: {linha[3]} | Idade: {linha[4]} | CPF: {linha[5]}")

# 6. Fechamento da conexão
conexao.close()

