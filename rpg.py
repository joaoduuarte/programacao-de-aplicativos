dano = int(input("qual dano voce deseja causar? "))
vida = int(input("o vilao tem quantos de vida?"))


subtracao = vida - dano


print(dano)
print(vida)
print("a vida do vilao agora é:", subtracao)


if dano >7:
    print("o dano causado foi grave")
elif dano <4:
    print("o dano foi fui suficiente")