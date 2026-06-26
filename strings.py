import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS professores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    materia TEXT,
    idade INTEGER,
    cpf TEXT UNIQUE,
    salario REAL,
    escola TEXT,
    endereco TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    turma TEXT,
    idade INTEGER,
    cpf TEXT UNIQUE,
    endereco TEXT,
    cidade TEXT,
    estado TEXT,
    professor_id INTEGER,
    FOREIGN KEY(professor_id) REFERENCES professores(id)
)
""")

conexao.commit()

def cadastrar_professor():

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    materia = input("Matéria: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    salario = float(input("Salário: "))
    escola = input("Nome da escola: ")
    endereco = input("Endereço: ")

    comando = f"""
    INSERT INTO professores
    (nome,telefone,materia,idade,cpf,salario,escola,endereco)

    VALUES
    ('{nome}','{telefone}','{materia}',{idade},
    '{cpf}',{salario},'{escola}','{endereco}')
    """

    cursor.execute(comando)
    conexao.commit()

    print("\nProfessor cadastrado!\n")


def listar_professores():

    cursor.execute("SELECT * FROM professores")

    dados = cursor.fetchall()

    print("\n------ PROFESSORES ------\n")

    for p in dados:

        print(f"""
ID: {p[0]}
Nome: {p[1]}
Telefone: {p[2]}
Matéria: {p[3]}
Idade: {p[4]}
CPF: {p[5]}
Salário: {p[6]}
Escola: {p[7]}
Endereço: {p[8]}
""")


def alterar_professor():

    id = int(input("ID do professor: "))

    nome = input("Novo nome: ")
    telefone = input("Novo telefone: ")
    materia = input("Nova matéria: ")
    idade = int(input("Nova idade: "))
    cpf = input("Novo CPF: ")
    salario = float(input("Novo salário: "))
    escola = input("Nova escola: ")
    endereco = input("Novo endereço: ")

    comando = f"""
    UPDATE professores SET

    nome='{nome}',
    telefone='{telefone}',
    materia='{materia}',
    idade={idade},
    cpf='{cpf}',
    salario={salario},
    escola='{escola}',
    endereco='{endereco}'

    WHERE id={id}
    """

    cursor.execute(comando)

    conexao.commit()

    print("\nProfessor alterado!\n")


def excluir_professor():

    id = int(input("ID do professor: "))

    cursor.execute(f"DELETE FROM professores WHERE id={id}")

    conexao.commit()

    print("\nProfessor excluído!\n")

def cadastrar_aluno():

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    turma = input("Turma: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")

    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    print("\nLista de Professores")
    cursor.execute("SELECT id, nome FROM professores")
    professores = cursor.fetchall()

    for p in professores:
        print(f"ID: {p[0]} - {p[1]}")

    professor = int(input("Digite o ID do professor: "))

    comando = f"""
    INSERT INTO alunos
    (nome,telefone,turma,idade,cpf,endereco,cidade,estado,professor_id)

    VALUES
    ('{nome}','{telefone}','{turma}',{idade},
    '{cpf}','{endereco}','{cidade}','{estado}',{professor})
    """

    cursor.execute(comando)

    conexao.commit()

    print("\nAluno cadastrado!\n")

def listar_alunos():

    cursor.execute("""

    SELECT alunos.id,
           alunos.nome,
           alunos.telefone,
           alunos.turma,
           alunos.idade,
           alunos.cpf,
           alunos.endereco,
           alunos.cidade,
           alunos.estado,
           professores.nome

    FROM alunos

    LEFT JOIN professores

    ON alunos.professor_id = professores.id

    """)

    alunos = cursor.fetchall()

    print("\n------ ALUNOS ------\n")

    for a in alunos:

        print(f"""
ID: {a[0]}
Nome: {a[1]}
Telefone: {a[2]}
Turma: {a[3]}
Idade: {a[4]}
CPF: {a[5]}
Endereço: {a[6]}
Cidade: {a[7]}
Estado: {a[8]}
Professor: {a[9]}
""")

def alterar_aluno():

    id = int(input("ID do aluno: "))

    nome = input("Novo nome: ")
    telefone = input("Novo telefone: ")
    turma = input("Nova turma: ")
    idade = int(input("Nova idade: "))
    cpf = input("Novo CPF: ")

    endereco = input("Novo endereço: ")
    cidade = input("Nova cidade: ")
    estado = input("Novo estado: ")

    print("\nProfessores cadastrados")

    cursor.execute("SELECT id,nome FROM professores")

    professores = cursor.fetchall()

    for p in professores:
        print(f"{p[0]} - {p[1]}")

    professor = int(input("Novo ID do professor: "))

    comando = f"""

    UPDATE alunos SET

    nome='{nome}',
    telefone='{telefone}',
    turma='{turma}',
    idade={idade},
    cpf='{cpf}',
    endereco='{endereco}',
    cidade='{cidade}',
    estado='{estado}',
    professor_id={professor}

    WHERE id={id}

    """

    cursor.execute(comando)

    conexao.commit()

    print("\nAluno alterado!\n")

def excluir_aluno():

    id = int(input("ID do aluno: "))

    cursor.execute(f"DELETE FROM alunos WHERE id={id}")

    conexao.commit()

    print("\nAluno excluído!\n")


def menu():

    while True:

        print("     SISTEMA DA ESCOLA")
        print("1 - Professores")
        print("2 - Alunos")
        print("3 - Listar Tudo")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção: ")

        
        if opcao == "1":

            while True:

                print("\n------ PROFESSORES ------")
                print("1 - Cadastrar")
                print("2 - Listar")
                print("3 - Alterar")
                print("4 - Excluir")
                print("5 - Voltar")

                op = input("Escolha: ")

                if op == "1":
                    cadastrar_professor()

                elif op == "2":
                    listar_professores()

                elif op == "3":
                    alterar_professor()

                elif op == "4":
                    excluir_professor()

                elif op == "5":
                    break

                else:
                    print("Opção inválida!")

        
        elif opcao == "2":

            while True:

                print("\n------ ALUNOS ------")
                print("1 - Cadastrar")
                print("2 - Listar")
                print("3 - Alterar")
                print("4 - Excluir")
                print("5 - Voltar")

                op = input("Escolha: ")

                if op == "1":
                    cadastrar_aluno()

                elif op == "2":
                    listar_alunos()

                elif op == "3":
                    alterar_aluno()

                elif op == "4":
                    excluir_aluno()

                elif op == "5":
                    break

                else:
                    print("Opção inválida!")

        
        elif opcao == "3":

            print("\n------ PROFESSORES ------")
            listar_professores()

            print("\n------ ALUNOS -----")
            listar_alunos()

    
        elif opcao == "4":

            print("\nPrograma encerrado!")

            conexao.close()

            break

        else:
            print("Opção inválida!")


menu()

def cadastrar_professor():

    try:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        materia = input("Matéria: ")
        idade = int(input("Idade: "))
        cpf = input("CPF: ")
        salario = float(input("Salário: "))
        escola = input("Nome da escola: ")
        endereco = input("Endereço: ")

        comando = f"""
        INSERT INTO professores
        (nome,telefone,materia,idade,cpf,salario,escola,endereco)

        VALUES
        ('{nome}','{telefone}','{materia}',{idade},
        '{cpf}',{salario},'{escola}','{endereco}')
        """

        cursor.execute(comando)
        conexao.commit()

        print("\nProfessor cadastrado!\n")

    except ValueError:
        print("\nErro: Idade e salário tem que ser numero.")

    except sqlite3.IntegrityError:
        print("\nErro: CPF já cadastrado.")

    except Exception as erro:
        print(f"\nErro inesperado: {erro}")

    finally:
        print("Operação finalizada.\n")
