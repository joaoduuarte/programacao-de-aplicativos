import sqlite3


def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escolar.db')

    cursor = conexao.cursor()

    # O Python reclama de "Incorrect number of bindings"
    # Estamos passando a variável, por que ocorre o erro?

    cursor.execute(
        "SELECT nome FROM professores WHARE id = ?",
        (id_prof)
    )

    resultado = cursor.fetchone()
    print(resultado)

    conexao.close()
   