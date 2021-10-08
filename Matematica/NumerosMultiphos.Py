#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 08/10/2021                               #
#    PROJETO: DESCOBRIR SE O NUMERO É MULTIPLO.     #
#                                                   #
#####################################################

import math

Parametros = {
    
    "Inicio" : 1,
    "Fim" : 100,
    "NumerosMultiplo" : 10,
    
    }

while (Parametros["Inicio"] <=  Parametros["Fim"]):
    if (Parametros["Inicio"] % Parametros["NumerosMultiplo"] == 0):
        print("O numero ", Parametros["Inicio"], " é multiplo de ", Parametros["NumerosMultiplo"])
    Parametros["Inicio"] += 1
