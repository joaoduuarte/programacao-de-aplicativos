nota = float(input("qual sua nota?"))

presença = int(input("qual sua presença"))

if nota >= 7.0 and presença >= 75:
    print("parabens voce foi aprovado")
elif nota < 7.0 and presença < 75:
    print("reprovado, verifique suas notas.")