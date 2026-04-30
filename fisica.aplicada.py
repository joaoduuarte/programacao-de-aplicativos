def converter_km_para_ms(velocidade):
    return velocidade / 3.6

vel = float(input("digite sua velocidade de km/h: "))

if vel > 80:
    ms = converter_km_para_ms(vel)
    print(f"velocidade {ms:.2f} ms/s. reduza a velocidade! ")
else:
    print("velocidade no limite")
