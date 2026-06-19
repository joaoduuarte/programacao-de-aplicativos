import sqlite3


BANCO_DADOS = 'escola_demonstracao.db'

def cadastrar():
    print("\n--- Novo Cadastro ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    turma = input("Turma: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    id_professor = int(input("Id Professor: "))

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    comando = f'''
        INSERT INTO alunos (nome, telefone, turma, idade, cpf, id_professor)
        VALUES ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}', {id_professor})
    '''

    cursor.execute(comando)
    conexao.commit()
    print("Aluno cadastrado com sucesso!")
    conexao.close()  

def listar():
    print("\n--- Lista de Alunos ---")
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    # Read usando SELECT
    cursor.execute("SELECT * FROM alunos")
    todos_alunos = cursor.fetchall()

    if not todos_alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for a in todos_alunos:
            print(f"ID: {a[0]} | Nome: {a[1]} | Turma: {a[3]} | CPF: {a[5]}")

    conexao.close()

def atualizar():
    print("\n--- Atualizar Dados ---")
    id_busca = int(input("Digite o ID do aluno que deseja editar: "))

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    # Primeiro, verificamos se o ID existe
    cursor.execute(f"SELECT * FROM alunos WHERE id = {id_busca}")
    aluno = cursor.fetchone() # Busca apenas uma linha

    if not aluno:
        print("Aluno não encontrado.")
        conexao.close()
        return

    print(f"Editando dados de: {aluno[1]}")
    novo_nome = input(f"Novo Nome ({aluno[1]}): ")
    novo_tel = input(f"Novo Telefone ({aluno[2]}): ")
    nova_turma = input(f"Nova Turma ({aluno[3]}): ")
    nova_idade = input(f"Nova Idade ({aluno[4]}): ")
    novo_cpf = input(f"Novo CPF ({aluno[5]}): ")
    novo_id_professor = int(input(f"Novo ID Professor ({aluno[6]}): "))

    comando = f'''
        UPDATE alunos 
        SET nome = '{novo_nome}', telefone = '{novo_tel}', turma = '{nova_turma}', 
            idade = {nova_idade}, cpf = '{novo_cpf}', id_professor = {novo_id_professor}
        WHERE id = {id_busca}
    '''
    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    print("Dados atualizados com sucesso!")

def excluir():
    print("\n--- Excluir Aluno ---")
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    # Delete usando o comando DELETE FROM do SQL baseado no ID
    comando = f"DELETE FROM alunos WHERE id = {id_busca}"
    
    cursor.execute(comando)
    conexao.commit()

    conexao.close()

# --- MENU PRINCIPAL ---
def menu():
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            turma TEXT,
            idade INTEGER,
            cpf TEXT UNIQUE NOT NULL,
            id_professor INTEGER,
            FOREIGN KEY (id_professor) REFERENCES professores(id)
        )
    ''')

    conexao.commit()
    conexao.close()

    while True:
        print("\n=== SISTEMA ESCOLAR (SQLITE) ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()