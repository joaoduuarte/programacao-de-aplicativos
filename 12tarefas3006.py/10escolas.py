import sqlite3 
 
def deletar_escola_antiga(): 
    id_escola = int(input("ID da escola a remover: ")) 
    conexao = sqlite3.connect('sistema_escola.db') 
	#cursor = conexao.cursor() 
     
	# Esse comando vai apagar o banco inteiro se o aluno não prestar atenção.
     
    #cursor.execute("DELETE FROM escolas WHERE id = id_escola") 
     
    conexao.commit() 
    conexao.close() 

#codigo certo

import sqlite3

def deletar_escola_antiga():
    try:
        id_escola = int(input("ID da escola a remover: "))

        conexao = sqlite3.connect("sistema_escola.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola,))

        conexao.commit()

        if cursor.rowcount > 0:
            print("Escola removida com sucesso!")
        else:
            print("Nenhuma escola encontrada com esse ID.")

    except ValueError:
        print("Erro: o ID deve ser um número inteiro.")

    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

    finally:
        try:
            conexao.close()
        except NameError:
            pass

deletar_escola_antiga()

#O código pede o ID da escola, conecta ao banco de dados e executa o comando DELETE para excluir a escola correspondente.
#  O try/except trata erros, como quando o usuário digita um ID inválido ou ocorre um problema no banco.
#  O commit() salva a alteração, 
# rowcount verifica se a escola foi realmente removida e o finally garante que a conexão com o banco seja fechada.





