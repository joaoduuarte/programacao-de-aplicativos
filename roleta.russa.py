senha = input(" digite sua senha :")
tentativas = int(input(" digite quantas tentativas voce tentou :"))
token = (" possui token ? (s/n)")

if senha == "admin123" and (tentativas % 3 == 0 or token == "s"):
    print(f" tentativa N {tentativas}, acesso permitido")
else:
    print(F"tentativa N {tentativas}, acesso negado")