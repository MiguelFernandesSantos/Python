#---------------------------------------------#
#                                             #
#  Nome: Miguel Fernandes Santos              #
#  Projeto: Solicita a entrada de numeros     #
#  e calcula a media entre eles.              #
#                                             #
#                                             #
#---------------------------------------------#

numeros = {
                "MenorQueDez" : 0,
                "MenorQueCem" : 0,
                "MenorQueMil" : 0,
                "MenorQueDezMil" : 0,
                "MaiorQueDezMil" : 0,
                "QtsTotal" : 0,
                "Soma" : 0,
                "Media" : 0,
            }

Num = 1

while (Num != 0):

    Num = float(input("Digite um numero: "))
    if (Num == 0):
        break

    elif (Num < 0):
        print("\nO numero inserido é um numero negativo, por favor insira um numero positivo.")
        break

    elif (Num >= 1 and Num <= 9):
        numeros["MenorQueDez"] += 1

    elif (Num >= 10 and Num <= 99):
        numeros["MenorQueCem"] += 1

    elif (Num >= 100 and Num <= 999):
        numeros["MenorQueMil"] += 1

    elif (Num >= 1000 and Num <= 10000):
        numeros["MenorQueDezMil"] += 1

    else:
        numeros["MaiorQueDezMil"] += 1

    numeros["Soma"] += Num

numeros["QtsTotal"] = numeros["MenorQueDez"] + numeros["MenorQueCem"] + numeros["MenorQueMil"] + numeros["MenorQueDezMil"] +numeros["MaiorQueDezMil"]

if numeros["QtsTotal"] != 0:
    numeros["Media"] = numeros["Soma"] / numeros["QtsTotal"]
    print("\nVoce digitou " + str(numeros["MenorQueDez"]) + " numeros que estao entre 1 e 9.")
    print("\nVoce digitou " + str(numeros["MenorQueCem"]) + " numeros que estao entre 10 e 99.")
    print("\nVoce digitou " + str(numeros["MenorQueMil"]) + " numeros que estao entre 100 e 999.")
    print("\nVoce digitou " + str(numeros["MenorQueDezMil"]) + " numeros que estao entre 1000 e 10000.")
    print("\nVoce digitou " + str(numeros["MaiorQueDezMil"]) + " numeros maiores que 10000.")
    print("\nA soma dos numeros é de " + str(numeros["Soma"]))
    print("\nA media dos numeros é de " + str(numeros["Media"]))

else:
    print("\nVoce não digitou nenhum numero.")
