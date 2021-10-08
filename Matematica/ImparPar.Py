#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 08/10/2021                               #
#    PROJETO: DESCOBRIR SE É IMPAR OU PAR.          #
#                                                   #
#####################################################

import math

Numeros = [44, 86, 15, 16, 75, 90, 656, 25, 153, 165, 813, 32, 36]

ImparPar = {
    
    "Impar" : 0,
    "ImparSoma" : 0,
    "ImparMedia" : 0,
    "Par" : 0,
    "ParSoma" : 0,
    "ParMedia" : 0,

    }

for item in Numeros:
    if item % 2 == 0:
        ImparPar["Par"] += 1
        ImparPar["ParSoma"] += item
    else:
        ImparPar["Impar"] +=  1
        ImparPar["ImparSoma"] += item

ImparPar["ParMedia"] = round(ImparPar["ParSoma"] / ImparPar["Par"],2)
ImparPar["ImparMedia"] = round(ImparPar["ImparSoma"] / ImparPar["Impar"],2)

print("Total de numeros impares: ", ImparPar["Impar"])
print("Total de numeros Pares: ", ImparPar["Par"])
print("Soma de numeros impares: ", ImparPar["ImparSoma"])
print("Soma de numeros Pares: ", ImparPar["ParSoma"])
print("Media de numeros impares: ", ImparPar["ImparMedia"])
print("Media de numeros pares: ", ImparPar["ParMedia"])
