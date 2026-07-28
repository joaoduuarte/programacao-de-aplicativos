import sqlite3 
 
def cadastrar_serie_seguro(nome, id_escola): 
    try: 
    	# Se a linha abaixo falhar por falta de permissão na pasta, 
    	# o bloco 'finally' vai tentar fechar algo que não abriu. Como corrigir? 
        conexao = sqlite3.connect('/pasta_protegida/sistema.db') 
    	#cursor = conexao.cursor() 
        #cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome, id_escola)) 
        conexao.commit() 
    except sqlite3.Error as e: 
        print("Erro técnico:", e) 
    finally: 
        conexao.close() 

#codigo certo

import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None

    try:
        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
            (nome, id_escola)
        )

        conexao.commit()

    except sqlite3.Error as e:
        print("Erro técnico:", e)

    finally:
        if conexao:
            conexao.close()

#A variável conexao começa como None. Se a conexão for criada com sucesso, ela recebe o objeto do banco.
#  No finally, o programa verifica se existe uma conexão antes de tentar fechá-la,
#  evitando um erro caso a abertura do banco tenha falhado.