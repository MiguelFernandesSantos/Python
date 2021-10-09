#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 09/10/2021                               #
#    PROJETO: INTEIROS AO QUADRADO.                 #
#                                                   #
#####################################################

from random import randrange, uniform
import math

# DECLARAÇÃO DE UM ARRAY:
numeros = [None for _ in range(13)]

# VARIAVEL UTILIZADA PARA PERCORRER O ARRAY E ADICIONAR VALORES:
tamanho = len(numeros) - 1

# VARIAVEL PARA PERCORRER O ARRAY:
i = 0

while(i <= tamanho):
    # A POSIÇÃO DO VALOR I RECEBE UM VALOR ENTRE 10 E 99
    numeros[i] = (randrange(1, 100))
    # MOSTRA NO CONSOLE SEM PULAR LINHA O VALOR GERADO ALEATORIO:
    print("O numero gerado é: ", numeros[i])
    # FAZ A POTENCIA DO VALOR GERADO ALEATORIO:
    numeros[i] = numeros[i] * numeros[i]
    # MOSTRA NO CONSOLE O VALOR DA POTENCIA:
    print("A sua potencia é:", numeros[i], "\n")
    i += 1
