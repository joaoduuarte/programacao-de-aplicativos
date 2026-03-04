cargo =str(input("qual seu cargo ? "))
codigo = int(input("digite o codigo de acesso: "))
escolha = input ("botao de emergencia (s/n)")
protecao = input("equipamento de protecao completa (s/n)")

if (cargo == "engenheiro" or cargo == "tecnico") and (codigo == 1234 or escolha == "s") and protecao == "s":
    print("acesso liberado")
else:
    print("acesso negado")