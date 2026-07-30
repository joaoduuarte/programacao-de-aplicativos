import sqlite3

def inserir_escola(nome):
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO escolas (nome) VALUES (?)",
        (nome,)
    )

    conexao.commit()
    conexao.close()

#O problema é que a conexão com o banco (conexao) e o cursor (cursor) foram criados fora da função, ficando como variáveis globais.

#Isso pode causar problemas quando o sistema cresce e usa vários arquivos (módulos), porque:

#vários módulos podem tentar usar a mesma conexão ao mesmo tempo;
#a conexão pode ser fechada em um arquivo e outro tentar usá-la depois;
#fica mais difícil controlar erros e liberar recursos;
#o código fica dependente de uma variável externa, deixando a manutenção mais complicada.