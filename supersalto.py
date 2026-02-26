nivel = int(input("qual seu nivel atual? "))

esferas = int(input("quantas esferas coletada voce tem ?"))

if nivel >= 20 and esferas >= 50:
    print("parabens, voce desbloqueou o super salto")
elif nivel < 20 and esferas < 50:
    print ("insuficiente para desbloquear habilidade")