comando = ""

# O laço continuará enquanto o usuário NÃO digitar 'sair'
while comando.lower() != "sair":
    comando = input("Digite algo (ou 'sair' para encerrar): ")
    
    if comando.lower() != "sair":
        print(f"Você digitou: {comando}")

print("Programa encerrado com sucesso!")