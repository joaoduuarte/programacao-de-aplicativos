status = input ("digite seu status")
vagas =[ "Ocupado", "Livre", "Ocupado", "Livre"]
numero = int(input("digite um numero de 0 a 3 : "))

if vagas %2 ==0 and status == "livre":
    print(f"vaga {vagas}")
else:
    print(f"vaga{1} não autorizada")

