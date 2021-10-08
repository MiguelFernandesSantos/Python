#####################################################
#                                                   #
#    NOME: MIGUEL FERNANDES SANTOS.                 #
#    DATA: 08/10/2021                               #
#    PROJETO: CALCULO AREA E PERIMETRO (DIDATICO).  #
#                                                   #
#####################################################

def tudo (formas ={}):

    quadrado = CalcularQuadrado(formas["Quadrado"])
    triangulo = CalcularTriangulo(formas["Triangulo"])
    retangulo = CalcularRetangulo(formas["Retangulo"])
    circulo = CalcularCirculo(formas["Circulo"])
    losango = CalcularLosango(formas["Losango"])
    trapezio = CalcularTrapezio(formas["Trapezio"])
    paralelogramo = CalcularParalelogramo(formas["Paralelogramo"])

    tudo =  {
                    "Quadrado" : quadrado ,
                    "Triangulo" : triangulo ,
                    "Retangulo" : retangulo ,
                    "Circulo" : circulo ,
                    "Losango" : losango ,
                    "Trapezio" : trapezio ,
                    "Paralelogramo" : paralelogramo 
                }

    return tudo

def CalcularQuadrado(quadrado = {}):
    # CALCULA A AREA DO QUADRADO ( BASE * ALTURA):
    quadrado["Area"] = quadrado["Base"] * quadrado["Altura"]

    # CALCULA O PERIMETRO DO QUADRADO (BASE * 2) + ( ALTURA * 2):
    quadrado["Perimetro"] = (quadrado["Base"] * 2) + (quadrado["Altura"] * 2)

    # DECLARAÇÃO DE UMA MATRIZ:
    AreaPerimetro = [None for _ in range(2)]

    # O PRIMEIRO VALOR DO ARRAY (INDICE 0) RECEBE O VALOR DA AREA:
    AreaPerimetro[0] = quadrado["Area"]

    # O SEGUNDO VALOR DO ARRAY (INDICE 1) RECEBE O VALOR DO PERIMETRO:
    AreaPerimetro[1] = quadrado["Perimetro"]


    return AreaPerimetro

def CalcularTriangulo (triangulo = {}):
    # CALCULA A AREA DO TRIANGULO ((BASE * ALTURA) / 2):
    triangulo["Area"] = (triangulo["Base"] * triangulo["Altura"]) / 2

    # CALCULA O PERIMETRO DO TRIANGULO (LADO1 + LADO2 + LADO3):
    triangulo["Perimetro"] = triangulo["Lado1"] + triangulo["Lado2"] + triangulo["Lado3"]

    # DECLARAÇÃO DE UMA MATRIZ:
    AreaPerimetro = [None for _ in range(2)]

    # O PRIMEIRO VALOR DO ARRAY (INDICE 0) RECEBE O VALOR DA AREA:
    AreaPerimetro[0] = triangulo["Area"]

    # O SEGUNDO VALOR DO ARRAY (INDICE 1) RECEBE O VALOR DO PERIMETRO:
    AreaPerimetro[1] = triangulo["Perimetro"]

    return AreaPerimetro;

def CalcularRetangulo (retangulo = {}):
    # CALCULA A AREA DO RETANGULO (BASE * ALTURA):
    retangulo["Area"] = retangulo["Base"] * retangulo["Altura"]

    # CALCULA O PERIMETRO DO RETANGULO ((BASE * 2) + (ALTURA * 2)):
    retangulo["Perimetro"] = (retangulo["Base"] * 2) + (retangulo["Altura"] * 2)

    # DECLARAÇÃO DE UM ARRAY:
    AreaPerimetro = [None for _ in range(2)]

    # O PRIMEIRO VALOR (INDICE 0) RECEBE O VALOR DA AREA:
    AreaPerimetro[0] = retangulo["Area"]

    # O SEGUNDO VALOR (INDICE 1) RECEBE O VALOR DO PERIMETRO:
    AreaPerimetro[1] = retangulo["Perimetro"]

    return AreaPerimetro;

def CalcularCirculo (circulo = {}):
    # CALCULA A AREA DO CIRCULO (PI *(DIAMETRO / 2) * (DIAMETRO / 2)):
    circulo["Area"] = circulo["Pi"] * ( (circulo["Diametro"] / 2) * (circulo["Diametro"] / 2 ))

    # CALCULA O PERIMETRO DO CIRCULO ((2 * PI) * (DIAMETRO / 2)):
    circulo["Perimetro"] = (2 * circulo["Pi"]) * (circulo["Diametro"] / 2)

    # DECLARAÇÃO DE UM ARRAY:
    AreaPerimetro = [None for _ in range(2)]

    # O PRIMEIRO VALOR (INDICE 0) RECEBE O VALOR DA AREA:
    AreaPerimetro[0] = circulo["Area"]

    # O SEGUNDO VALOR (INDICE 1) RECEBE O VALOR DO PERIMETRO:
    AreaPerimetro[1] = round(circulo["Perimetro"], 1)

    return AreaPerimetro

def CalcularLosango (losango = {}):
    # CALCULA A AREA DO LOSANGO ((DIAGONAL MENOR * DIAGONAL MAIOR) / 2):
    losango["Area"] = (losango["DiagonalMenor"] * losango["DiagonalMaior"]) / 2

    # CALCULA O PERIMETRO DO LOSANGO (LADO * 4):
    losango["Perimetro"] = losango["Lado"] * 4

    # DECLARAÇÃO DE UM ARRAY:
    AreaPerimetro = [None for _ in range(2)]

    # O PRIMEIRO VALOR (INDICE 0) RECEBE O VALOR DA AREA:
    AreaPerimetro[0] = losango["Area"]

    # O SEGUNDO VALOR (INDICE 1) RECEBE O VALOR DO PERIMTRO:
    AreaPerimetro[1] = losango["Perimetro"]

    return AreaPerimetro

def CalcularTrapezio (trapezio = {}):
    # CALCULA O VALOR DA AREA DO TRAPEZIO (((BASE MAIOR + BASE MENOR) / 2) * ALTURA))):
    trapezio["Area"] = ((trapezio["BaseMaior"] + trapezio["BaseMenor"]) / 2) * trapezio["Altura"]

    # CALCULA O VALOR DO PERIMETRO DO TRAPEZIO (BASE MAIOR + BASE MENOR + LADO1 + LADO2):
    trapezio["Perimetro"] = trapezio["BaseMaior"] + trapezio["BaseMenor"] + trapezio["Lado1"] + trapezio["Lado2"]

    # DECLARAÇÃO DE UM ARRAY:
    AreaPerimetro = [None for _ in range(2)]

    # O PRIMEIRO VALOR (INDICE 0) DO ARRAY RECEBE O VALOR DA AREA:
    AreaPerimetro[0] = trapezio["Area"]

    # O SEGUNDO VALOR (INDICE 1) DO ARRAY RECEBE O VALOR DO PERIMETRO:
    AreaPerimetro[1] = trapezio["Perimetro"]

    return AreaPerimetro

def CalcularParalelogramo (paralelogramo = {}):
    # CALCULA A AREA DO PARALELOGRAMO (BASE * ALTURA):
    paralelogramo["Area"] = paralelogramo["Base"] * paralelogramo["Altura"];

    # CALCULA O PERIMETRO DO PARALELOGRAMO ((BASE * 2) + (ALTURA * 2)):
    paralelogramo["Perimetro"] = (paralelogramo["Base"] * 2) + (paralelogramo["Altura"] * 2);

    # DECLARAÇÃO DE UM ARRAY:
    AreaPerimetro = [None for _ in range(2)]

    # O PRIMERIO VALOR (INDICE 0) RECEBE O VALOR DA AREA:
    AreaPerimetro[0] = paralelogramo["Area"];

    # O SEGUNDO VALOR (INDICE 1) RECEBE O VALOR DO PERIMETRO:
    AreaPerimetro[1] = paralelogramo["Perimetro"];

    return AreaPerimetro;



GeometriaPlana = { 
					"Quadrado" : {

									# Base x altura
									"Base" : 10,
									"Altura" : 10,
									"Area" : 0,
									"Perimetro" : 0,

									},

					"Triangulo" : {

									#(Base x altura) / 2 
									"Base" : 10,
									"Altura" : 10,
									"Lado1" : 5,
									"Lado2" : 5,
									"Lado3" : 5,
									"Area" : 0,
									"Perimetro" : 0,

									},

					"Retangulo" : {

									# Base x altura
									"Base" : 10,
									"Altura" : 10,
									"Area" : 0,
									"Perimetro" : 0,

									},

					"Circulo" : {

									# Pi x raio²
									"Diametro" : 20,
									"Raio" : 0,
									"Pi" : 3.14,
									"Area" : 0,
									"Perimetro" : 0,

									},

					"Losango" :{

									# (Diagonal maior x Diagonal menor) /2
									"DiagonalMaior" : 10,
									"DiagonalMenor" : 10,
									"Lado" : 5,
									"Area" : 0,
									"Perimetro" : 0,

									},

					"Trapezio" : {

									# ((BaseMaior + BaseMenor) / 2) * Altura
									"BaseMaior" : 10,
									"BaseMenor" : 10,
									"Lado1" : 5,
									"Lado2" : 5,
									"Altura" : 10,
									"Area" : 0,
									"Perimetro" : 0,

									},

					"Paralelogramo" : {

									# Base x altura
									"Base" : 10,
									"Altura" : 10,
									"Area" : 0,
									"Perimetro" : 0,

										}
			}

Calculos = tudo(GeometriaPlana)

print("  A | P")
print(Calculos["Quadrado"])
print(Calculos["Triangulo"])
print(Calculos["Retangulo"])
print(Calculos["Circulo"])
print(Calculos["Losango"])
print(Calculos["Trapezio"])
print(Calculos["Paralelogramo"])
