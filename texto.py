import sqlite3

try:
    # Tenta conectar a um banco de dados de teste na memória
    conexao = sqlite3.connect(':memory:')
    cursor = conexao.cursor()
    
    # Executa um comando simples para pedir a versão do SQLite
    cursor.execute("SELECT sqlite_version();")
    versao = cursor.fetchone()[0]
    
    print("O SQLite está funcionando perfeitamente no Python!")
    print(f"Versão instalada: {versao}")
    
    conexao.close()
except Exception as e:
    print(f"Houve um erro ao tentar usar o SQLite: {e}")