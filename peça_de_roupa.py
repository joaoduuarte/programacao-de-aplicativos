comprimento = input("o seu comprimento esta entre 10cm e 12cm?  (s/n)")
largura = input (" seu comprimento esta entre 5cm ou 2cm?  (s/n)")

if (comprimento == "s"):
    print (f"peça aprovada")
else:
    print(f"REPROVADO: problema no comprimento")

if (largura == "s"):
    print(f"peça aprovada")
else:
    print(f"REPROVADO: problema na largura")