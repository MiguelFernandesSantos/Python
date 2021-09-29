#---------------------------------------------#
#                                             #
#  Nome: Miguel Fernandes Santos              #
#  Projeto: Gerar dez números inteiros        #
#  aleatórios e apresentar como saída:        #
#   - a soma dos números pares                #
#   - a soma dos números ímpares              #
#                                             #
#---------------------------------------------#

from random import randrange, uniform

Aleatorio = 0
SomaPares = 0
SomaImpares = 0

for cont in range(1, 10):
    Aleatorio = (randrange(1, 100))
    print("O numero gerado aleatorio é: ", Aleatorio)

    if Aleatorio % 2 == 0:

        print("E ele é um numero Par")
        SomaPares = SomaPares + Aleatorio
        print("")

    else:

        print("E ele é um numero impar")
        SomaImpares = SomaImpares + Aleatorio
        print("")

print("")
print("A soma dos numeros Pares é de: ", SomaPares)
print("A soma dos numeros Impares é de: ", SomaImpares)
