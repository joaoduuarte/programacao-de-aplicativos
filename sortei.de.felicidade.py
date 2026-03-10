print("------ SORTEIO DE FIDELIDADE-----")
id =  input("qual seu id")
valor = int(input("valor da compra ?" ))

if id % 2 == 0 and valor > 500:
    print(f"Parabéns, usuário {id}! Você ganhou um cupom para sua compra de {valor}")
else:
    print(f"Obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções!")