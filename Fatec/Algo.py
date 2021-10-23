# Dicionario com 3 listas e 1 string:
Dados = {
        
        "Numeros" : [],
        "Pesos" : [],
        "Atuais" : [None for _ in range(2)],
        "Menu" : ""

        }

# Enquanto o usuario nao digitar SAIR ou 2:
while (Dados["Menu"] != "Sair" or Dados["Menu"] != "2"):
    
    # Menu:
    print("\n-------- MENU --------")
    print(" 1 - Entrada \n 2 - Sair")
    print("-------- MENU --------")

    # Escolha do usuario:
    menu = input("\nO que deseja fazer?\n")

    # Se o usuario decidir sair:
    if (menu == "Sair" or menu == "2"):
        break

    # Entrada de valores:
    Dados["Atuais"][0] = input("\n\nDigite um numero para a amostra: ")
    Dados["Atuais"][1] = input("\nDigite o peso do valor anterior: ")


    # Tentar converter:
    try:
        Dados["Atuais"][0] = float(Dados["Atuais"][0])
        Dados["Atuais"][1] = float(Dados["Atuais"][1])

        Dados["Numeros"].append(Dados["Atuais"][0])
        Dados["Pesos"].append(Dados["Atuais"][1])
    
    # Se nao conseguir mostrar que o valor é invalido:
    except:
        print("O valor digitado anteriormente não é um numero valido. \n\n ")

print (Dados["Numeros"])
print (Dados["Pesos"])
