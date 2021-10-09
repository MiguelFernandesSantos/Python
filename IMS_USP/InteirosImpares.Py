#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 09/10/2021                               #
#    PROJETO: INTEIROS IMPARES.                     #
#                                                   #
#####################################################

from random import randrange, uniform

# DECLARAÇÃO DA VARIAVEL UTILIZADA PARA MOSTRAR OS NUMEROS IMPARES_
# MENORES OU IGUAL A ELA
limite = (randrange(10, 20))

# VARIAVEL QUE GUARDA OS NUMEROS IMPARES:
auxiliar = 1

while (auxiliar <= limite):
    # A CADA VEZ QUE O LAÇO SE INICIA É COLOCADO NO CONSOLE O NUMERO:
    print(auxiliar)
    # A CADA VEZ QUE O LAÇO SE INICIA É ADICIONADO + 2 A VARIAVEL:
    auxiliar += 2
    
