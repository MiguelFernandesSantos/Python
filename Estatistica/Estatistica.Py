#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 08/10/2021                               #
#    PROJETO: ESTATISTICA.                          #
#                                                   #
#####################################################

import math

def CalculaTudo (Numeros =[], Pesos =[]):
	
	Tudo = [None for _ in range(8)]
	Tudo[0] = MediaSimples(Numeros)
	Tudo[1] = MediaPonderada(Numeros, Pesos)
	Tudo[2] = PrimeiroQuartil(Numeros)
	Tudo[3] = SegundoQuartil(Numeros)
	Tudo[4] = TerceiroQuartil(Numeros)

	return Tudo

# FUNÇÃO PARA CALCULAR A MEDIA SIMPLES:
def MediaSimples (numeros = []):
	
	tamanho = len(numeros)
	media = 0
	
	for item in numeros:
		media += item

	media = media / tamanho

	return media

# FUNÇÃO PARA CALCULAR A MEDIA PONDERADA:
def MediaPonderada(numeros = [], pesos = []):

	somaValores = 0
	somaPesos = 0
	Auxiliar = 0
	indice = 0

	for item in numeros:
		Auxiliar = item * pesos[indice]
		somaValores += Auxiliar
		somaPesos += pesos[indice]
		indice += 1

	Auxiliar = somaValores / somaPesos

	return Auxiliar

# FUNÇÃO PARA ENCONTRAR O PRIMEIRO QUARTIL:
def PrimeiroQuartil (numeros = []):

	numeros.sort()

	quantidade = len(numeros)

	numeroExato =  quantidade / 4

	min = round(numeroExato, 0)
	max = 0

	if min > numeroExato:
		max = min
		min = min - 1
	else:
		max = min + 1

	if (numeroExato > min and numeroExato < max):
		numeroExato = math.floor(numeroExato)

	return numeros[numeroExato]

# FUNÇÃO PARA ENCONTRAR O SEGUNDO QUARTIL:
def SegundoQuartil (numeros = []):


	quantidade = len(numeros)
	numeroExato = quantidade / 2
	indice = 0

	min = round(numeroExato, 0)
	max = 0

	numeros.sort()

	if min > numeroExato:
		max = min
		min = min - 1
	else:
		max = min + 1

	if (numeroExato > min and numeroExato < max):
		numeroExato = math.floor(numeroExato)

	return numeros[numeroExato]

# FUNÇÃO PARA ENCONTRAR O TERCEIRO QUARTIL:
def TerceiroQuartil (numeros = []):

	numeros.sort()

	quantidade = len(numeros)

	quantidade =  quantidade  * 3

	numeroExato = quantidade / 4

	min = round(numeroExato, 0)
	max = 0

	if min > numeroExato:
		max = min
		min = min - 1
	else:
		max = min + 1

	if (numeroExato > min and numeroExato < max):
		numeroExato = math.floor(numeroExato)

	return numeros[numeroExato]



Numeros = [ 10, 10, 1, 45, 63, 74, 32, 67, 31, 54, 21, 56, 23]
Pesos = [1, 2, 3, 5, 6, 1, 8, 1, 2, 4, 2, 6, 3]
Quantidade = []
Variancias = []
VarianciasQuadrada = []

tudo = CalculaTudo(Numeros, Pesos)

for item in tudo:
	print(item)
