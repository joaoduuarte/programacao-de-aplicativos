nome = (input("qual seu nome?"))

altura = float(input("qual seu altura?"))

if altura >=1.50:
    print("acesso liberado, divirta-se", nome)
elif altura < 1.50:
    print("acesso negado", nome)
