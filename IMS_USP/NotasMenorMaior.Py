#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 09/10/2021                               #
#    PROJETO: MAIOR E MENOR NOTA.                   #
#                                                   #
#####################################################

from random import randrange, uniform

# DECLARAÇÃO DE UM ARRAY PARA AS NOTAS DOS ALUNOS:
alunosNotas = [None for _ in range(4)]

# DECLARAÇÃO DE DUAS VARIAVEIS PARA O LAÇO:
tamanho = len(alunosNotas) - 1
i = 0

# LAÇO DE REPETIÇÃO PARA PERCORRER O ARRAY:

while(i <= tamanho):
    alunosNotas[i] =(randrange(1, 11))
    print ("Notas: ", alunosNotas[i])
    i += 1

# DECLARAÇÃO DE VARIAVEL PARA GUARDAR A MAIOR NOTA;
maior = 0

# DECLARAÇÃO DE VARIAVEL PARA GUARDAR A MENOR NOTA;
menor = alunosNotas[3]

i = 0

while (i <= tamanho):
     # SE O VALOR DA VARIAVEL MAIOR SER MENOR QUE O VALOR DO ARRAY:
     if maior < alunosNotas[i]:
        # MAIOR RECEBE O VALOR DO ARRAY
        maior = alunosNotas[i]
        

     # SE O VALOR DA VARIAVEL MENOR SER MAIOR QUE O VALOR DO ARRAY:
     if menor > alunosNotas[i]:
        # MENOR RECEBE O VALOR DO ARRAY:
        menor = alunosNotas[i];
     
     i += 1

print("\nMaior: ", maior, "  Menor: ", menor);
