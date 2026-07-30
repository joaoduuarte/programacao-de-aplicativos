import sqlite3


def vincular_aluno_turma():
    nome = input("Nome do aluno: ")

    # Captura erros de entrada do usuário e erros do banco de dados.
    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
            (nome, id_turma)
        )

        conexao.commit()

    except ValueError:
        print("Erro: digite apenas um número para o ID da turma.")

    except sqlite3.Error:
        print("Erro no banco de dados!")

    finally:
        if 'conexao' in locals():
            conexao.close()

#O problema principal era que o código tentava capturar apenas erros do SQLite usando `except sqlite3.Error`.
# Porém, o erro causado quando o usuário digitava um valor inválido, como "Turma B" no lugar de um número,
# não era um erro do banco de dados. Esse caso gerava um `ValueError`, que acontecia na conversão feita pelo `int()`.
# Como esse tipo de erro não estava sendo tratado, o programa era encerrado.
