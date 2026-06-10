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



print("Passo 3: Dados da Ana Clara gravados com sucesso!")
