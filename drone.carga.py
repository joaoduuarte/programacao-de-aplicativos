print ("---- SEJA BEM VINDO AO SISTEMA DE POUSO! -------")

codigo = int(input("Digite o código do drone: "))
autorizacao = input(("Possui autorização da torre? (s/n): "))

if codigo == 999 or autorizacao == "s":

    # 1. FASE DE ANALISE DE VOO
    bateria = int(input("Nível de bateria (0 a 100): "))
    clima = input(("Clima (ensolarado/chuvoso): "))
    vento = int(input("Velocidade do vento (km/h): "))

    # 2. EMERGENCIA 
    if bateria > 10:
        print("POUSO AUTORIZADO: Iniciando descida.")

    else:
        # 3. ANALISE DE VOO
        if (clima == "ensolarado" and vento < 30) or (clima == "chuvoso" and vento < 10):
            print("POUSO AUTORIZADO: Iniciando descida.")
        else:
            print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.")
    