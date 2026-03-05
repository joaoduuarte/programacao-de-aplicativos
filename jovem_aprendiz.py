curso = input("voce concluiu o curso (s/n)? ")

if (curso == "n"):
    print (f"acesso negado")
else :
    instrutor = input("o instrudor esta na sala? (s/n)")
    if instrutor == "s":
        print(f"acesso permitido")
    else:
        print("acesso negado")