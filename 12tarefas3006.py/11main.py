import sqlite3 
 
def listar_alunos_e_turmas(): 
    conexao = sqlite3.connect('sistema_escola.db') 
	#cursor = conexao.cursor() 
     
	# O relatório roda, mas repete os dados erroneamente em formato de matriz cruzada 
	# porque falta definir a regra de colagem (vínculo). Conserte o comando SQL: 

# codigo certo 

import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT alunos.nome, turmas.nome
        FROM alunos
        INNER JOIN turmas
        ON alunos.turma_id = turmas.id
    """)

    resultados = cursor.fetchall()

    for aluno, turma in resultados:
        print(f"Aluno: {aluno} | Turma: {turma}")

    conexao.close()

listar_alunos_e_turmas()

#O problema é que a consulta provavelmente está fazendo um JOIN sem informar como as tabelas se relacionam,
# o que gera uma matriz cruzada (produto cartesiano), repetindo os dados.

#O correto é usar a cláusula ON para definir o vínculo entre as tabelas.
