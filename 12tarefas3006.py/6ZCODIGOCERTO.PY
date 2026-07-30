import sqlite3


def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escolar.db')

    cursor = conexao.cursor()

    # Busca o professor pelo ID informado
    cursor.execute(
        "SELECT nome FROM professores WHERE id = ?",
        (id_prof,)
    )

    resultado = cursor.fetchone()
    print(resultado)

    conexao.close()

#O problema principal estava na forma como o valor do parâmetro era enviado para a consulta SQL.
#  O código utilizava `(id_prof)` em vez de uma tupla, então o Python interpretava apenas como uma variável comum,
#  e não como uma lista de valores para substituir o `?` do comando SQL. Para corrigir,
#  foi necessário usar `(id_prof,)`, com a vírgula, criando uma tupla com um único valor.
#Além disso, havia erros de escrita no comando SQL, como `WHARE` em vez de `WHERE`,
# e uma vírgula colocada de forma incorreta após o ponto de interrogação.
# Esses erros impediam a execução correta da consulta e causavam o problema de quantidade incorreta de parâmetros
#  (*Incorrect number of bindings*).
