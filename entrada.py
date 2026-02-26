idade = int(input("qual sua idade? "))

saldo = float(input("qual seu saldo? "))

if idade >= 18 and saldo >= 50.0:
    print("acesso autorizado, bem vindo ao evento")
elif idade < 18 and saldo < 50.0:
    print("infelizmente voce nao cumpre os requisitos para entrada")