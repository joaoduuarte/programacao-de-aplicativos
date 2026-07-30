import sqlite3

def cadastrar_escola_manual():
    # O aluno resolveu gerar o ID por conta própria
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash).
    # Aplique a blindagem protetora necessária:
    cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola,))

#CODIGO CERTO

import sqlite3


def cadastrar_escola_manual():
    # O aluno resolveu gerar o ID por conta própria
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash).
    # Aplique a blindagem protetora necessária:

    try:
        cursor.execute(
            "INSERT INTO escolas (id, nome) VALUES (?, ?)",
            (id_escola, nome)
        )

        conexao.commit()

    except sqlite3.IntegrityError:
        print("Erro: este ID já está cadastrado.")

    finally:
        conexao.close()

#O erro acontecia porque o comando SQL precisava de dois valores (`id` e `nome`), 
# mas o código enviava apenas o ID, causando erro de quantidade de parâmetros.
#  Além disso, a tentativa de cadastrar um ID já existente gerava um `IntegrityError`,
#  que não era tratado e encerrava o programa.
#  A correção foi enviar os dois valores corretamente e adicionar tratamento para evitar a quebra do sistema.
