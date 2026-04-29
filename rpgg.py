vida = 100

def sofrer_dano(valor_dano):
    global vida
    vida -= valor_dano
    return vida

while vida > 0:
    try:
        dano = int(input("Quanto de dano o monstro causou? "))
        
        vida_atual = sofrer_dano(dano)
        
        if vida_atual < 0:
            print("Vida restante: 0")
        else:
            print(f"Vida restante: {vida_atual}")
            
    except ValueError:
        print("Por favor, digite um número válido.")

print("Game Over")