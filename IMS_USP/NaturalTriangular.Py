#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 09/10/2021                               #
#    PROJETO: NATURAL TRIANGULAR.                   #
#                                                   #
#####################################################

from random import randrange, uniform

# DICIONARIO PARA OS VALORES:
valores = {
                "Numero": 0 ,
                "Num1": 0 ,
                "Num2": 1 ,
                "Num3": 0 ,
                "Valor": 0,
                "Triangular": bool
          }

# GUARDAR NA VARIAVEL NUMERO UM NOVO NUMERO ALEATORIO ENTRE 1 E 10:
valores["Numero"] = (randrange(4, 25))

while(valores["Valor"] < valores["Numero"]):
    valores["Num1"] = valores["Num2"]
    valores["Num2"] = valores["Num1"] + 1
    valores["Num3"] = valores["Num2"] + 1
    # FAZ A MULTIPLICAÇÃO DE 3 NUMEROS SEGUIDOS (1 * 2 * 3):
    valores["Valor"] = valores["Num1"] * valores["Num2"] * valores["Num3"]

    if valores["Valor"] == valores["Numero"]:
        # COLOCA NO CONSOLE A MENSAGEM QUE O PRODUTO DA MULTIPLICAÇÃO DE 3 NUMEROS SEGUIDOS É IGUAL O VALOR GERADO ALEATORIO:
        print(valores["Num1"], " * ", valores["Num2"], " * ", valores["Num3"], " = ", valores["Numero"])
        valores["Triangular"] = True

# MOSTRA NO CONSOLE QUE O NUMERO NÃO É TRIANGULAR:
if valores["Triangular"] != True:
    print("O numero ", valores["Numero"], " não é um natural triangular.")
       

        
