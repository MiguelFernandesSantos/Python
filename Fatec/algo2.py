######################################################
#        TRABALHO FINAL - OFICINA DE PYTHON          #
#                                                    #
#    NOMES: DAVID GALVÃO MANDU DA SILVA;             #
#           MIGUEL FERNANDES SANTOS.                 #
#                                                    #
#    DATA: --/--/2021                                #
#    PROJETO: CÁLCULOS DE ESTATÍSTCA BÁSICA.         #
#                                                    #
######################################################

import math
from datetime import date

# ##############PROCEDIMENTOS##############

# GERAR ARQUIVO TXT:
def arquivo(valores = [], dados = []):
    data_atual = date.today()

    with open('Estatistica.txt', 'w+') as arquivos:
        arquivos.write("Data atual: " + str(data_atual) + "\n")
        arquivos.write("Base de dados: ")

        for item in dados:
            arquivos.write(str(item) + ", ")
        
        arquivos.write("\n\n------- Calculos -------\n")
        for item in valores:
            arquivos.write(str(item) + "\n")
            



#             1 - MÉDIA ARITMÉTICA SIMPLES
def mediasimples(valores=()):
    media = 0

    for item in valores:
        media += item

    media = media / qtde_elementos
    frase = 'Média Aritmética Simples = ' + str(media)
    return frase
#####################################################


#             2 - MÉDIA ARITMÉTICA PONDERADA
def mediaponderada(valores=()):
    valorxpesos = 0
    soma_peso = 0

    for item in valores:
        peso = int(input(f'Digite o peso do valor {item}: '))
        valorxpesos += (peso * item)
        soma_peso += peso

    media_ponderada = valorxpesos / soma_peso
    frase = 'Média Aritmética Ponderada =' + str(media_ponderada)
    return frase
#####################################################


#             3 - MODA
def moda(valores=()):
    dic = {item: 0 for item in valores}
    for item in valores:
        if item in dic.keys():
            dic[item] += 1
    valor_moda = [item for item in dic.values()]
    resultado_moda = [numero for numero in dic.keys() if dic[numero] == max(valor_moda) and max(valor_moda) > 1]

    if len(resultado_moda) != 0:
        frase = 'Moda = ' + str(resultado_moda)
    else:
        frase = 'Amostra Amodal'

    return frase
#####################################################


#             4 - MEDIANA
def mediana(valores=()):
    if qtde_elementos % 2 == 0:
        med = (valores[int((qtde_elementos / 2) - 1)] + valores[int((qtde_elementos / 2))]) / 2
        frase = 'Mediana = ' + str(med)
    else:
        med = valores[int((qtde_elementos / 2))]
        frase = 'Mediana = ' + str(med)

    return frase
#####################################################


#             5 - PRIMEIRO QUARTIL
def primeiroquartil(valores=()):
    if qtde_elementos % 4 == 0:
        q1 = (valores[int((qtde_elementos / 4) - 1)] + valores[int((qtde_elementos / 4))]) / 2
        frase = 'Primeiro Quartil = ' + str(q1)
    else:
        q1 = valores[int((qtde_elementos / 4))]
        frase = 'Primeiro Quartil = ' + str(q1)

    return frase
#####################################################


#             6 - TERCEIRO QUARTIL
def terceiroquartil(valores=()):
    if (3 * qtde_elementos) % 4 == 0:
        q3 = (valores[int((3 * qtde_elementos / 4) - 1)] + valores[int((3 * qtde_elementos / 4))]) / 2
        frase = 'Terceiro Quartil = ' + str(q3)
    else:
        q3 = valores[int(((3 * qtde_elementos) / 4))]
        frase = 'Terceiro Quartil = ' + str(q3)

    return frase
#####################################################


#             7 - AMPLITUDE
def amplitude(valores = ()):
    maior = max(valores)
    menor = min(valores)
    amplitude = maior - menor

    frase = 'Amplitude = ' + str(amplitude)

    return frase
#####################################################


#             8 - DESVIO-PADRÃO
def desvioPadrao (valores = ()):
    media = 0
    tamanho = len(valores) - 1
    indice = 0
    valor = 0
    soma = 0
    variancias = [None for _ in range(tamanho + 1)]
    varianciasQuadrada = [None for _ in range(tamanho + 1)]
    
    for item in valores:
        media += item

    media = media / (tamanho + 1)

    for item in valores:
        valor = item - media
        variancias[indice] = valor
        indice += 1

    indice = 0

    for item in variancias:
        valor =  item * item
        varianciasQuadrada[indice] = valor
        indice += 1

    soma = sum(varianciasQuadrada)
    soma = soma / tamanho  
    soma = math.sqrt(soma)

    frase = 'Desvio Padrão = ' + str(soma)

    return frase
#####################################################


#             9 - TUDO
def tudo (valores = ()):
    dados = [None for _ in range(8)]
    dados[0] = mediasimples(valores)
    dados[1] = mediaponderada(valores)
    dados[2] = moda(valores)
    dados[3] = mediana(valores)
    dados[4] = primeiroquartil(valores)
    dados[5] = terceiroquartil(valores)
    dados[6] = amplitude(valores)
    dados[7] = desvioPadrao(valores)

    return dados

# #################INÍCIO DO PROGRAMA################
qtde_elementos = int(input('Digite a quantidade de elementos da amostra: '))
elementos = []
dados = []

for elemento in range(0, qtde_elementos):
    valor = int(input(f'Digite o {elemento+1}º valor: '))
    elementos.append(valor)

# ==================MENU DE ESCOLHA==================
print('''
                 ---MENU---
    | 1 - Média Aritmética Simples
    | 2 - Média Aritmética Ponderada
    | 3 - Moda
    | 4 - Mediana
    | 5 - Primeiro Quartil
    | 6 - Terceiro Quartil
    | 7 - Amplitude
    | 8 - Desvio-Padrão
    | 9 - Calcular Tudo
    | 0 - Encerrar
    
    ''')
menu = int(input('Digite o número da Opção desejada: '))

# =============EXECUÇÃO DOS PROCEDIMENTOS============
if menu == 1:
    dados.append(mediasimples(elementos))
    arquivo(dados, elementos)
elif menu == 2:
    dados.append(mediaponderada(elementos))
    arquivo(dados, elementos)
elif menu == 3:
    dados.append(moda(elementos))
    arquivo(dados, elementos)
elif menu == 4:
    dados.append(mediana(elementos))
    arquivo(dados, elementos)
elif menu == 5:
    dados.append(primeiroquartil(elementos))
    arquivo(dados, elementos)
elif menu == 6:
    dados.append(terceiroquartil(elementos))
    arquivo(dados, elementos)
elif menu == 7:
    dados.append(amplitude(elementos))
    arquivo(dados, elementos)
elif menu == 8:
    dados.append(desvioPadrao(elementos))
    arquivo(dados, elementos)
elif menu == 9:
    dados = tudo(elementos)
    arquivo(dados, elementos)
else:
    print("Opção invalida.")
