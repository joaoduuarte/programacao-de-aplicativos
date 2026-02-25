valor_total = float(input("qual o valor da sua compra? "))
cupom = input("digite o cupom")


desconto = valor_total *0.10
novo_preco = valor_total - desconto


if cupom == "DEV10":
    print("seu cupom foi aplicado", desconto)
else:
    print("cupom invalido", novo_preco)