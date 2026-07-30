import sqlite3

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT , 
            nome TEXT NOT NULL  
        )
    ''')

# falta o commit
# temabem nao tem banco de dados


    

