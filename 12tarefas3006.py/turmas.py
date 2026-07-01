import sqlite3

def cadastrar_turma(nome,id_series,id_prof):

conexao = sqlite3.connect('sistema_escolas.db')
cursosr = conexao.cursor()
curssr.execute("PRAGMA foreign_keys = ON; ")

#se o id_prof não existir, ocorre um intefrityerror.
#se o error acontecer, o que ocorre com linha conexao.close()?

cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALEUS (?, ?, ?)", (nome, id_serie, id_prof))
conexao.commit()
conexao.close()