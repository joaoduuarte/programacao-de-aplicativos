import sqlite3

def cadastrar_serie(nome_serie,id_escolar):
    conexao = sqlite3.connect('sistema_escola.db')
    cursosr = conexao.cursosr()
    #o aluno tenta cadastra uma serie com id_escola = 999 (que nao existe).
    # o sqlite aceita o cadastro mesmo assim . O que esta faltando ativar?
    try: 
        cursosr.execute("INSERT INTO series (nomes_serie, id _escola) VALEUS  (?, ?)",
(nome_serie, id_escolar))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("error : escola inexistnte!")
    finally:
        conexao.close()

# o erro desse codigo É a falta da chave estrangeira ( foreign keys)
 
print("==== codigo certo ====")

import sqlite3

def cadastrar_serie(nome_serie, id_escolar):
    conexao = sqlite3.connect('sistema_escola.db')
    
    conexao.execute("PRAGMA foreign_keys = ON;")
    
    cursor = conexao.cursor()
    
    try: 
        
        cursor.execute("INSERT INTO series (nomes_serie, id_escola) VALUES (?, ?)", 
                       (nome_serie, id_escolar))
        conexao.commit()
        print("Série cadastrada com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()