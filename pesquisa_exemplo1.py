# cadastrando um professor 
nome = input("Nome do aluno: ")
idade = int(input("Idade: "))
turma = input("Turma: ")
id_professor = int(input("ID do professor responsável: "))

cursor.execute("""
INSERT INTO aluno
(nome, idade, turma, id_professor)
VALUES (?, ?, ?, ?)
""", (nome, idade, turma, id_professor))

conexao.commit()

#listar um professor especifico
id_professor = int(input("Digite o ID do professor: "))

cursor.execute("""
SELECT nome, turma
FROM aluno
WHERE id_professor = ?
""", (id_professor,))

alunos = cursor.fetchall()

for aluno in alunos:
    print(aluno)

#buscar o professor de um aluno 
id_aluno = int(input("Digite o ID do aluno: "))

cursor.execute("""
SELECT aluno.nome,
       professor.nome_completo
FROM aluno
INNER JOIN professor
ON aluno.id_professor = professor.id
WHERE aluno.id = ?
""", (id_aluno,))

resultado = cursor.fetchone()

print(resultado)

#listar um professor e a quantidade de aluno 
cursor.execute("""
SELECT professor.nome_completo,
       COUNT(aluno.id) AS quantidade_alunos
FROM professor
LEFT JOIN aluno
ON professor.id = aluno.id_professor
GROUP BY professor.id
""")

dados = cursor.fetchall()

for dado in dados:
    print(dado)