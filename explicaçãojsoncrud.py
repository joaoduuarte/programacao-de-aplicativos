import json
#import json importa o módulo JSON do Python para converter, ler e salvar dados em formato JSON.
import os
#import os importa o módulo OS do Python para interagir com o sistema operacional, como acessar arquivos, pastas e comandos do sistema.


BANCO_DADOS = 'alunos.json'
#BANCO_DADOS = 'alunos.json' cria uma variável que armazena o nome do arquivo JSON usado como banco de dados.

def cadastrar():
    #def cadastrar(): cria uma função chamada cadastrar, onde você pode colocar comandos para serem executados depois.

    print("\n--- Novo Cadastro ---")
    #mostra na tela o texto --- Novo Cadastro --- e \n pula uma linha antes da mensagem.
    
    if os.path.exists(BANCO_DADOS):
        #verifica se o arquivo ou caminho armazenado em BANCO_DADOS existe no sistema antes de continuar o código.

        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            #abre o arquivo indicado em BANCO_DADOS para leitura ('r'), usando codificação UTF-8, e cria a variável f para acessar o conteúdo dentro do bloco.
            
            alunos = json.load(f)
            #lê o conteúdo do arquivo f (em formato JSON) e transforma em um objeto Python, guardando o resultado na variável alunos.

    else:
        #indica a parte do código que será executada caso a condição do if seja falsa.

        alunos = []
        #cria uma lista vazia chamada alunos, que pode depois armazenar dados (como nomes ou registros de estudantes).

    novo_aluno = {
        #inicia a criação de um dicionário em Python, ou seja, um conjunto de dados no formato chave: valor, que vai armazenar informações de um novo aluno.

        "nome": input("Nome: "),
        #define a chave "nome" no dicionário e pede ao usuário para digitar um valor no teclado; o que for digitado será armazenado como o nome do aluno.
        "telefone": input("Telefone: "),
        #cria a chave "telefone" no dicionário e guarda o valor digitado pelo usuário no teclado, que será o número de telefone do aluno.
        "turma": input("Turma: "),
        #cria a chave "turma" no dicionário e armazena o valor que o usuário digitar no teclado, representando a turma do aluno.
        "idade": int(input("Idade: ")),
        #cria a chave "idade" e guarda o valor digitado pelo usuário, mas convertendo para número inteiro (int), em vez de texto.
        "cpf": input("CPF: ")
        #cria a chave "cpf" no dicionário e armazena o valor digitado pelo usuário no teclado como texto.
    }
    #fecha o dicionário que estava sendo criado, finalizando o conjunto de dados do novo_aluno.
    
    alunos.append(novo_aluno)
    #adicionou o dicionário do aluno ao final de uma lista chamada alunos.

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
        #Essa linha abre o arquivo de texto para salvar as informaçõs.
        json.dump(alunos, f, indent=4, ensure_ascii=False)
        #Essa linha salva a lista de alunos no formato JSON, mantendo o arquivo super organizado com recuos (indent=4) e os acentos corretos (ensure_ascii=False).
        
    print("Aluno cadastrado com sucesso!")
    #Essa linha exibe uma mensagem na tela avisando que o cadastro deu certo.

def listar():
    #mantem o foco na criação da função de listagem

    print("\n--- Lista de Alunos ---")
    #Essa linha imprime um cabeçalho bonito no terminal para organizar a exibição dos dados.
    
    if os.path.exists(BANCO_DADOS):
        #Essa linha verifica se o arquivo do banco de dados realmente existe antes de tentar abrir, evitando que o programa dê erro caso esteja vazio.
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            #Essa linha abre o arquivo no modo de leitura ('r') de forma segura, garantindo que o Python consiga ler os acentos corretamente.
            alunos = json.load(f)
            #Essa linha converte o texto do arquivo JSON de volta para uma lista de dicionários no Python, deixando os dados prontos para uso.
    else:
        #indica a parte do código que será executada caso a condição do if seja falsa.
        alunos = []
        #cria uma lista vazia chamada alunos, que pode depois armazenar dados (como nomes ou registros de estudantes).

    if not alunos:
        #Essa linha verifica se a lista de alunos veio vazia de dentro do arquivo, ou seja, se o arquivo existe mas não tem ninguém cadastrado.
        print("Nenhum aluno cadastrado.")
        #Essa linha exibe a mensagem na tela caso a lista de alunos esteja vazia.
        return
        #Essa linha encerra a execução da função imediatamente e volta para o ponto onde ela foi chamada.

    for aluno in alunos:
        #Essa linha cria um laço que passa por cada aluno da lista, permitindo acessar os dados de um por um.
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")
        #Essa linha exibe na tela todos os dados do aluno atual formatados e organizados de forma bem clara.

def atualizar():
    #Essa linha cria o início de uma nova função no seu programa para modificar os dados de um aluno que já foi cadastrado antes.
    print("\n--- Atualizar Aluno ---")
    #Essa linha apenas exibe um título bonito e organizado na tela para avisar o usuário que ele entrou na área de alteração de dados.
    if not os.path.exists(BANCO_DADOS):
        #Essa linha verifica se o arquivo do banco de dados não existe, protegendo o seu programa para ele não tentar alterar dados que ainda nem foram criados.
        print("Nenhum aluno cadastrado no sistema.")
        #Essa linha exibe uma mensagem clara para o usuário, avisando que a alteração não pode ser feita porque o banco de dados ainda está vazio.
        return
         #Essa linha encerra a execução da função imediatamente e volta para o ponto onde ela foi chamada

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        #Essa linha abre o banco de dados em modo de leitura ('r'), pronta para carregar a lista de alunos e procurar quem você quer atualizar.
        alunos = json.load(f)
        #Esta linha converte o conteúdo do arquivo JSON de volta para uma lista de alunos dentro do Python, deixando os dados prontos para a alteração.
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: "))
    #Essa linha pede para o usuário digitar o número do CPF do aluno e já o converte para um número inteiro, para que você possa localizá-lo na lista.
    
    for aluno in alunos:
        #Essa linha cria um laço que vai passar de aluno em aluno dentro da lista, permitindo que você verifique um por um até encontrar o CPF que o usuário digitou.
            print(f"Editando dados de: {aluno['nome']}")
            #Essa linha exibe uma mensagem na tela mostrando o nome do aluno que foi encontrado, confirmando para o usuário que ele está alterando a pessoa certa.
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            #Essa linha pede um novo nome para o aluno
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            #esse linha pede o telefone do aluno
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            #essa linha pede a turma do aluno
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            #essa linha pede a idade do aluuno 
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            #essa linha pede o cpf do aluno
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                #Essa linha abre o arquivo do meu bande dados no modo de escrita ('w'),
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
             #Essa linha encerra a execução da função imediatamente e volta para o ponto onde ela foi chamada
            
    print("Aluno não encontrado.")
    #Essa linha de código avisa ao usuário que o aluno procurado não está cadastrado.

def excluir():
    #Essa linha inicia a criação de uma função para remover um aluno do seu sistema.
    print("\n--- Excluir Aluno ---")
    #Essa linha serve para organizar e enfeitar a tela do seu programa, criando um cabeçalho claro para o usuário.
    if not os.path.exists(BANCO_DADOS):
        #Essa linha verifica se o arquivo que guarda os dados dos alunos existe no computador antes de tentar abri-lo.
        print("Nenhum aluno cadastrado no sistema.")
        #Essa linha avisa ao usuário que o sistema está completamente vazio, sem nenhuma informação salva ainda.
        return
         #Essa linha encerra a execução da função imediatamente e volta para o ponto onde ela foi chamada

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        #Essa linha serve para abrir o seu arquivo de dados com segurança para ler as informações dos alunos salvos no computador.
        alunos = json.load(f)
        #Essa linha pega todo o texto que estava guardado dentro do arquivo e o transforma magicamente em uma lista ou dicionário que o Python consegue entender e mexer.
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    #Essa linha pede para o usuário digitar o número de identificação (ID) do aluno e já converte essa resposta em um número inteiro para que o programa possa fazer a busca.
    
    nova_lista = [a for a in alunos if a['id'] != id_busca]
    #Essa linha usa um recurso do Python chamado List Comprehension (compreensão de lista) para criar uma lista novinha em folha, trazendo todos os alunos, exceto aquele que tem o ID que você deseja apagar.
    
    if len(nova_lista) < len(alunos):
        #Essa linha serve para descobrir se o aluno digitado foi encontrado e removido com sucesso do sistema.
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            #Essa linha abre o seu arquivo de dados, mas agora com uma intenção diferente: ela se prepara para salvar e atualizar as informações, gravando a nova lista de alunos no computador.
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
            #Essa linha de código salva a sua lista atualizada de alunos de volta no arquivo do computador, gravando a exclusão de forma definitiva.
        print("Aluno removido com sucesso!")
        #Essa linha é a confirmação final que dá um desfecho positivo para o usuário, avisando que todo o processo funcionou e o aluno foi apagado do sistema.
    else:
        #indica a parte do código que será executada caso a condição do if seja falsa.
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()