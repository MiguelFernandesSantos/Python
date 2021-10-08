#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 08/10/2021                               #
#    PROJETO: CALCULO DO IMC.                       #
#                                                   #
#####################################################

import math

Dados = {
    
    "Pesos" : 80,
    "Altura" : 1.75,
    "IMC" : 0

    }

Dados["IMC"] = Dados["Pesos"] / (Dados["Altura"] * 2)
Dados["IMC"] = round(Dados["IMC"],2)

if (Dados["IMC"] < 18.5):
    print("O seu IMC é Classificado como: Magreza.")
    print("Seu IMC é: ", Dados["IMC"])
elif (Dados["IMC"] < 24.9):
    print("O seu IMC é Classificado como: Normal.")
    print("Seu IMC é: ", Dados["IMC"])
elif (Dados["IMC"] < 29.9):
    print("O seu IMC é Classificado como: Sobrepeso.")
    print("Seu IMC é: " + Dados["IMC"])
else:
    print("O seu IMC é Classificado como: Obesidade grave.");
    print("Seu IMC é: ", Dados["IMC"]);

