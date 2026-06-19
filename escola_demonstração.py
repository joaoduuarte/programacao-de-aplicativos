import sqlite3

campos = sqlite3.connect("cadastro_aluno.db")
cursor = campos.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS escola (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    materia TEXT,
    cpf TEXT,
    salario REAL,
    escola TEXT

    id_professor INTERGER,
    FOREIGN KEY (id_professor) REFERENCES professor
)
""")

campos.commit()


def cadastrar_professor():
    nome_completo = input("Digite seu nome completo: ")
    telefone = input("Digite seu telefone: ")
    materia = input("Digite a matéria que você apresenta: ")
    cpf = input("Digite seu CPF: ")
    
    try:
        salario = float(input("Digite seu salário: "))
    except ValueError:
        print("Salário inválido! Use apenas números.")
        return

    nome_escola = input("Digite o nome da escola em que você trabalha: ")

    cursor.execute("""
        INSERT INTO escola (nome, telefone, materia, cpf, salario, escola)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome_completo, telefone, materia, cpf, salario, nome_escola))

    campos.commit()
    print("Professor cadastrado com sucesso!")


def listar_professores():
    cursor.execute("SELECT * FROM escola")
    registros = cursor.fetchall()

    if not registros:
        print("Nenhum professor cadastrado.")
        return

    for professor in registros:
        print(f"\nID: {professor[0]}")
        print(f"Nome: {professor[1]}")
        print(f"Telefone: {professor[2]}")
        print(f"Matéria: {professor[3]}")
        print(f"CPF: {professor[4]}")
        print(f"Salário: {professor[5]}")
        print(f"Escola: {professor[6]}")
        print("-" * 30)


while True:
    print("menu")
    print("1 - Cadastrar professor")
    print("2 - Listar professores")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_professor()

    elif opcao == "2":
        listar_professores()

    elif opcao == "3":
        print("Encerrando programa")
        break

    else:
        print("Opção inválida! Tente novamente.")

campos.close()

