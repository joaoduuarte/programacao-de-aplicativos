def esta_na_lista(lista, nome_para_buscar):
    
    for item in lista:
        if item == nome_para_buscar:
            return "Encontrado!"

    return "Não disponível"

minha_lista = ["maçã", "banana", "uva", "laranja", "melancia"]

busca1 = "uva"
resultado1 = esta_na_lista(minha_lista, busca1)
print(f"Buscando '{busca1}': {resultado1}")

busca2 = "pera"
resultado2 = esta_na_lista(minha_lista, busca2)
print(f"Buscando '{busca2}': {resultado2}")

busca3 = input("Digite o nome da fruta que deseja buscar: ")
print(f"Resultado: {esta_na_lista(minha_lista, busca3)}")

    