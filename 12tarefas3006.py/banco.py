import sqlite3

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT , 
            nome TEXT NOT NULL  
        )
    ''')

# falta o commit
# temabem nao tem banco de dados

print("====== codigo certo =======")

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT , 
            nome TEXT NOT NULL  
        )
    ''')

def inicialização_banco():

    id = int(input("ID: "))
    nome = input("Nome: ")  # Resolvido o Erro 2: Agora a variável 'nome' existe!

    print(f"Cadastrado com sucesso: {nome} e ID: {id}")

cursor.execute()
conexao.commit()
    

