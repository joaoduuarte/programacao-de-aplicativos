codigo = int(input("Digite o código do pacote: "))
peso = float(input("Digite o peso do pacote (kg): "))

if peso > 50:
    status = "Carga Pesada"
elif peso < 5 and codigo % 10 == 0:
    status = "Entrega Expressa"
else:
    status = "Entrega Normal"

print(f"Pacote {codigo}: {status}")