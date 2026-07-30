import sqlite3

def verificar_registros():
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    registros = cursor.fetchall()

    print("Primeiro print:", registros)
    print("Segundo print:", registros)

    conexao.close()

verificar_registros()

#O problema acontece porque o comando fetchall() busca todos os registros da consulta e depois remove esses dados do cursor.
#  Ou seja, quando o primeiro print executa cursor.fetchall(), ele já pega todos os alunos encontrados e o cursor fica vazio.
#  Por isso, quando o segundo print tenta executar cursor.fetchall() novamente, não existem mais registros para mostrar.
#A solução é armazenar o resultado do fetchall() em uma variável.
#  Dessa forma, os dados são buscados uma única vez e podem ser utilizados várias vezes no programa.
#  Assim, os dois prints conseguem acessar a mesma informação sem perder os registros.

