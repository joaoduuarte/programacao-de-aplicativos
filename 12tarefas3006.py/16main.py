def menu(): 
    while True: 
        print("1. Cadastrar Aluno") 
        print("2. Sair") 
        opcao = input("Escolha: ") 
         
        if opcao == "1": 
            print("Cadastrando...") 
        elif opcao == "2": 
            print("Saindo do programa.") 
        	# Por que o programa continua rodando e mostrando o menu mesmo digitando 2? 
            pass 

# codigo certo

def menu():
    while True:
        print("1. Cadastrar Aluno")
        print("2. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print("Cadastrando...")

        elif opcao == "2":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()

#O problema acontecia porque o programa utilizava o comando pass quando o usuário escolhia a opção 2.
#  O pass não encerra o menu, ele apenas não executa nenhuma ação e permite que o while True continue repetindo.
#  Como o menu está dentro de um loop infinito, ele voltava a mostrar as opções novamente.

#A correção foi substituir o pass pelo comando break,
#  que interrompe o laço de repetição e permite que o programa seja encerrado quando o usuário escolher a opção "Sair".
#  Além disso, foi adicionada uma mensagem para tratar opções inválidas, deixando o menu mais seguro.



