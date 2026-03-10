# Pedir numero total de garrafa
garrafas = int(input("Digite o número total de garrafas processadas hoje: "))

# Verifica limpeza
if garrafas % 500 == 0:
    print("hora da limpeza: Parar máquina imediatamente!")

# Verifica controle de produção
if garrafas % 100 == 0:
    print("qualidade: Retirar amostra para teste.")

# Caso tenha erro na produção
if garrafas % 500 != 0 and garrafas % 100 != 0:
    print(f"Produção em dia. Garrafa número {garrafas} processada.")