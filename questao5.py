def inverter(palavra):
    forma_invertida = ""
    
    for i in range(len(palavra) - 1, - 1, -1):
        forma_invertida += palavra[i]
    return forma_invertida

forma_original = input("Digite uma string que deseja inverter: ")
forma_invertida = inverter(forma_original)
print("A string invertida é: ", forma_invertida)