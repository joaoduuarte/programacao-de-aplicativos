import sqlite3 
 
def listar_alunos_e_turmas(): 
    conexao = sqlite3.connect('sistema_escola.db') 
	#cursor = conexao.cursor() 
     
	# O relatório roda, mas repete os dados erroneamente em formato de matriz cruzada 
	# porque falta definir a regra de colagem (vínculo). Conserte o comando SQL: 

