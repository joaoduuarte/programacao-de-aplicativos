import sqlite3

def cadastrar_serie(nome_serie, id_escolar):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O aluno tenta cadastrar uma série com id_escola = 999 (que não existe).
    # O SQLite aceita o cadastro mesmo assim. O que está faltando ativar?
    try:
        cursor.execute(
            "INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
            (nome_serie, id_escolar)
        )
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: escola inexistente!")
    finally:
        conexao.close()

#O código apresentava erros de digitação, como `cursosr` em vez de `cursor`, `VALEUS` em vez de `VALUES`, 
# além de nomes de colunas escritos incorretamente e um espaço indevido em `id_escola`.
# Também havia erros ortográficos nos comentários e na mensagem exibida ao usuário.
# Após corrigir esses problemas e ajustar a indentação, o código passa a funcionar corretamente.
# No entanto, para que o SQLite impeça o cadastro de uma série com uma escola inexistente,
# é necessário ativar a verificação de chaves estrangeiras (`foreign_keys`), pois ela não é habilitada automaticamente.
