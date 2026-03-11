id = int(input("qual seu id?: ")) 
temperatura = float(input("digite a temperatura :"))
tempo = float(input("digite o tempo :"))

if id % 3 == 0 and (temperatura > 40 or tempo > 8):
    print(f"Funcionário {id}, você foi escalado para a manutenção preventiva hoje")
else:
    print("sua máquina opera dentro dos padrões normais.")