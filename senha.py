def validar_senha(senha):
    while len(senha) < 6:
        print("senha invalida ")
        senha = input("digite sua senha novamente ")
    if len(senha) >= 6:
        print("senha cadastrada com sucesso")

senha_usuario =input("digite sua senha")
validar_senha(senha_usuario)