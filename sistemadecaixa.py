saldo = 1000.00

print("=== Caixa Eletrônico ===")
print("1 - Depósito")
print("2 - Saque")
print("3 - Extrato")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    valor = float(input("Digite o valor para depósito: R$ "))
    
    if valor > 0:
        saldo += valor
        print(f"Depósito realizado com sucesso!")
        print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Erro: O valor do depósito deve ser maior que zero.")

elif opcao == 2:
    valor = float(input("Digite o valor para saque: R$ "))
    
    if valor > 0 and (valor <= saldo or valor == 100.00):
        saldo -= valor
        print("Saque realizado com sucesso!")
        print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Erro: Saque não autorizado.")

elif opcao == 3:
    print("=== Extrato ===")
    print(f"Saldo atual: R$ {saldo:.2f}")

else:
    print("Opção inválida.")                      