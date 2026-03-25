livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestadosv = []
escolha = input("digite o livro que voce deseja:")

if escolha in livros_disponiveis:
    livros_disponiveis.remove(escolha)
    livros_disponiveis.append(escolha)
else:
    print("desculpe,este livro nao esta no acervo")

devolucao = input("digite o nome do livro que esta devolvendo: ")
if escolha in livros_emprestadosv:
    livros_emprestadosv.remove(devolucao)
    livros_disponiveis.append(devolucao)
else:
    print("este livro não consta como emprestado")

del livros_emprestadosv[0:2]

print(f"estados final das duas listas {livros_disponiveis} e {livros_emprestadosv}.")