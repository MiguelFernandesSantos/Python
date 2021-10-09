#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 09/10/2021                               #
#    PROJETO: SOMA DOS NUMEROS INTEIROS.            #
#                                                   #
#####################################################

from random import randrange, uniform

# DECLARAÇÃO DE UM ARRAY:
numeros = [None for _ in range(13)]
# VARIAVEL UTILIZADA PARA PERCORRER O ARRAY E SABER QUANDO PARAR:
tamanho = len(numeros) - 1
# DECLARAÇÃO DE UMA VARIAVEL PARA FAZER A SOMA:
soma = 0
# VARIAVEL UTILIZADA PARA PERCORRER O ARRAY E ADICIONAR VALORES:
i = 0

while (i <= tamanho):
    # A POSIÇÃO DO VALOR I RECEBE UM VALOR ENTRE 10 E 99
    numeros[i] = (randrange(10, 100))
    # ADICIONA O NUMERO GERADO NA VARIAVEL SOMA:
    soma += numeros[i]
    # ADICIONA O NUMERO GERADO NA VARIAVEL SOMA:
    print("O numero gerado é: ", numeros[i] , "\n")
    i += 1

# MOSTRA NO CONSOLE O VALOR DA SOMA
print("A soma dos numeros é: ", soma)
