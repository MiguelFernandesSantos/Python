#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 08/10/2021                               #
#    PROJETO: CALCULO DO VOLUME (DIDATICO).         #
#                                                   #
#####################################################

import math

def Tudo (all = {}):
    # CONJUNTO DE DECLARAÇOES DE VARIAVEIS QUE RECEBEM O VALOR RETORNADOS DAS FUNÇÕES:
    cone = CalcularVolumeCone(all["Cone"])
    piramide = CalcularVolumePiramide(all["Piramide"])
    esfera = CalcularVolumeEsfera(all["Esfera"])
    cilindro = CalcularVolumeCilindro(all["Cilindro"])

    # DICIONARIO A SER RETORNADO CONTENDO OS VALORES DO VOLUME:
    calculo = {
                    "Cone": cone ,
                    "Piramide": piramide ,
                    "Esfera": esfera ,
                    "Cilindro": cilindro ,
                }

    return calculo


def CalcularVolumeCone (cone = {}):
   # CALCULA O VALOR DO RAIO AO QUADRADO DO CONE:
   cone["Raio"] = math.pow(cone["Raio"], 2)

   # CALCULA O VALOR DO VOLUME DO CONE ((RAIO * ALTURA) / 3):
   cone["Volume"] = (cone["Raio"] * cone["Altura"]) / 3
                
   return cone["Volume"]


def CalcularVolumePiramide (piramide = {}):
    # CALCULA A AREA DA BASE DA PIRAMIDE (LADO1 * LADO2):
    piramide["AreaBase"] = piramide["Lado1"] * piramide["Lado2"]

    # CALCULA O VOLUME DA PIRAMIDE ((AREA BASE * ALTUA) / 3):
    piramide["Volume"] = (piramide["AreaBase"] * piramide["Altura"]) / 3

    return piramide["Volume"]


def CalcularVolumeEsfera (esfera = {}):
    # CALCULA O VALOR DO RAIO³:
    esfera["Raio"] = math.pow(esfera["Raio"], 3)

    # CALCULA O VALOR DO RAIO / 3:
    esfera["Raio"] = esfera["Raio"] / 3

    # CALCULA O VOLUME DO RAIO (RAIO * 4):
    esfera["Volume"] = esfera["Raio"] * 4

    return esfera["Volume"]


def CalcularVolumeCilindro (cilindro = {}):
    #  CALCULA O QUADRADO DO RAIO DO CILINDRO:
    cilindro["Raio"] = math.pow(cilindro["Raio"], 2)

    # CALCULA O VOLUME DO CILINDRO (RAIO * ALTURA):
    cilindro["Volume"] = cilindro["Raio"] * cilindro["Altura"]

    return cilindro["Volume"]


formas = {
                # DICIONARIO QUE CONTEM AS INFORMAÇÕES DO CONE:
				"Cone" : {
							"Volume" : 0,
							"Raio" : 3,
							"Altura" : 8,

							},
                # DICIONARIO QUE CONTEM AS INFORMAÇÕES DA PIRAMIDE:
				"Piramide" : {

							"Volume" : 0,
							"Lado1" : 6,
							"Lado2" : 4,
							"Altura" : 8

							},
               # DICIONARIO QUE CONTEM AS INFORMAÇÕES DA ESFERA:
				"Esfera" : {

							"Volume" : 0,
							"Raio" : 6,

							},
                # DICIONARIO QUE CONTEM AS INFORMAÇÕES DO CILINDRO:
				"Cilindro" : {

							"Volume" : 0,
							"Raio" : 4,
							"Altura" : 10,

							},

		}

tudo = Tudo(formas)

for item in tudo:
    print("O " + item + " possui um volume de ", tudo[item])
