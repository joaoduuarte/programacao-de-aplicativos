peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc > 25:
    print("você esta acima do peso.")
else:
    print("você está abaixo do peso.")
