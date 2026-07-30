import sqlite3


def cadastrar_escola_rapido():
    nome = input("Digite o nome da escola: ")
    endereco = input("Digite o endereço: ")

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO escolas (nome, endereco) VALUES (?, ?)",
        (nome, endereco)
    )

    conexao.commit()
    conexao.close()

#O código estava errado porque utilizava uma f-string para inserir diretamente os valores digitados pelo usuário dentro do comando SQL.
# Essa prática é insegura, pois permite que uma pessoa mal-intencionada insira comandos SQL junto com os dados,
#  causando uma possível injeção de SQL.
#A forma correta é utilizar parâmetros com `?` no comando SQL e passar os valores separadamente.
# Dessa maneira, o SQLite entende os dados apenas como informações a serem armazenadas, evitando que sejam interpretados como comandos.
#Além disso, o uso de parâmetros torna o código mais seguro e segue uma boa prática no desenvolvimento de aplicações com banco de dados.
