import sqlite3 

def criar_tabela_turma(): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor()

     	# O SQLite acusa erro de sintaxe próximo ao FOREIGN KEY. Cadê o erro? 
    cursor.execute(''' 
    	CREATE TABLE IF NOT EXISTS turmas ( 
        	id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome_turma TEXT, 
            id_serie,  
        	FOREIGN KEY (id_serie) REFERENCES series(id) 
    	) 
	''') 
    conexao.commit() 
    conexao.close() 

#codigo certo

import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT,
            id_serie INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id)
        )
    ''')

    conexao.commit()
    conexao.close()

criar_tabela_turma()

#O SQLite estava acusando erro próximo ao FOREIGN KEY porque a linha anterior (id_serie) estava incompleta.
#  Toda coluna precisa ter uma definição, como TEXT, INTEGER, REAL, etc. Ao colocar id_serie INTEGER,
#  o banco consegue entender que essa coluna será usada como chave estrangeira que referencia o campo id da tabela series.
