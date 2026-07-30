import sqlite3


def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Cria a tabela impedindo CPF duplicado.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT UNIQUE
        )
    ''')

    try:
        cursor.execute(
            "INSERT INTO professores (nome, cpf) VALUES (?, ?)",
            (nome, cpf)
        )

        conexao.commit()

    except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado.")

    finally:
        conexao.close()

#O problema principal era que a tabela permitia cadastrar vários professores com o mesmo CPF,
#  pois a coluna cpf não possuía nenhuma restrição de unicidade.
#  Para impedir valores repetidos diretamente na estrutura da tabela, foi necessário adicionar a regra UNIQUE na coluna cpf.
#Também havia um erro de escrita: INTERGER estava incorreto, sendo o correto INTEGER.
#  Além disso, o código apenas criava a tabela, mas não realizava o cadastro do professor e não tratava possíveis erros caso 
# o CPF já existisse.
#Com a restrição UNIQUE, o próprio banco de dados passa a impedir CPFs duplicados,
#  e o try/except captura o erro para evitar que o programa seja encerrado.