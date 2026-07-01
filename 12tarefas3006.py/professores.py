import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect ('sistema_escolar.db')
    cursosr = conexao.cursor()

    #o python reclamar de "Incorect number of bindings"
    # Estamos passando a variavel, por que ocorre o erro?
    cursor.execute("SELECT  nome FROM  professores WHARE  id = ? , " (id_prof))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()

   # criou a variável cursosr, mas depois usou cursor. Os dois nomes precisam ser iguais.
#WHARE está escrito errado. O correto é WHERE.
#Está faltando uma vírgula entre a instrução SQL e o parâmetro id_prof.
#Como a consulta tem apenas um parâmetro, ele deve ser passado como uma tupla de um elemento: (id_prof,). Se você escrever apenas (id_prof),
#o Python entende que isso é apenas o valor entre parênteses, e não uma tupla. Por isso o SQLite gera o erro "Incorrect number of bindings supplied".

print("==== codigo certo =====")

import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect("sistema_escolar.db")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT nome FROM professores WHERE id = ?",
        (id_prof,)
    )

    resultado = cursor.fetchone()

    if resultado:
        print("Professor:", resultado[0])
    else:
        print("Professor não encontrado.")

    conexao.close()

# Exemplo de uso
buscar_professor(1)