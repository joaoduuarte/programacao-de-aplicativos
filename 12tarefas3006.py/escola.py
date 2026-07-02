import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a promover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor():