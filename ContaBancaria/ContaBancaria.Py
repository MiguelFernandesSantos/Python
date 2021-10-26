#---------------------------------------------#
#                                             #
#  Nome: Miguel Fernandes Santos              #
#  Projeto: Conta bancaria.                   #
#                                             #
#---------------------------------------------#

# Importa a biblioteca para conseguir pegar a data atual:
from datetime import date


# função para retornar o valor do credito que vc possue direito:
def SeuCredito (salario):
    
    # Cria uma lista com 3 valores que se iniciam em 0:
    dados = [0 for _ in range (3)]
    
    # Credito de 50% a mais:
    dados[0] = ((salario / 100) * 50) + salario
    
    # Credito de 75% a mais:
    dados[1] = ((salario / 100) * 75) + salario
    
    # Credito de 100% a mais:
    dados[2] = ((salario / 100) * 100) + salario
    
    return dados


####################################################################################

# função para gerar arquivo txt do extrato na mesma pasta que o arquivo:
def Extrato (valores = {}, nome = ""):
    
    # Pega a data atual:
    Data = date.today()
    
    # Pega a quantidade total de valores no historico: 
    Tamanho = len(valores["Historico"])
    
    # Abre um documento chamado 'extrato.txt':
    with open('extrato.txt', 'w+') as extrato:
        # Escreve no documento a data atual:
        extrato.write("Data atual: " + str(Data) + "\n")
        # Escreve no documento o nome:
        extrato.write("Nome: " + str(nome) + "\n")
        # Escreve no documento o Saldo atual:
        extrato.write("Saldo atual: " + str(valores["Saldo"]) + "\n")
        # Escreve no documento o Credito atual:
        extrato.write("Credito atual: " + str(valores["Credito"]) + "\n")
        # Escreve no documento o credito a pagar atual:
        extrato.write("Credito a Pagar: " + str(valores["CreditoPagar"]) + "\n")
        
        # Se existir algo no historico
        if (Tamanho > 0):
            extrato.write("\n\n---------- HISTORICO ---------\n")
            # escrever cada uma das informaçoes do historico:
            for historico in valores["Historico"]:
                extrato.write(str(historico) + "\n")


        
####################################################################################

# Adiciona no historico de transaçoes:
def Historico (palavra, valor,):
    
    # Pega a data Atual:
    Data = date.today()
    # Declara a variavel frase:
    Frase = ""
    
    # A variavel frase recebe a data mais o tipo de movimento mais o valor:
    Frase = str(Data) + " - Foi " + palavra + " um valor de " + str(valor)
    
    return Frase



####################################################################################

# função para retirar o dinheiro:
def Retirar (valor, saldo):
    
    # Se o saldo for menor que o valor a retirar:
    if (saldo < valor):
        print("Infelizmente o valor que deseja retirar é maior que o seu saldo atual.")
        return saldo
        
    else:
        saldo = saldo - valor
    
    return saldo



####################################################################################

# função para adicionar valor a sua conta:
def Adicionar (valor, saldo):
    # adiciona saldo:
    saldo = saldo + valor
    
    return saldo



####################################################################################

# função para pedir credito:
def Credito (valor,credito, saldo, divida):
    
    # Cria uma lista com 3 valores que se iniciam em 0
    dados = [0 for _ in range(3)]
    
    # Se seu credito for menor que o valor que vc deseja retirar:
    if (valor > credito):
        print("\nInfelizmente seu credito é menor que o necessario!!!")
        return dados
    
    # indice 0 é o saldo atual + o credito:
    dados[0] = valor
    # indice 1 é o valor de credito que tem que pagar:
    dados[1] = divida + valor
    # indice 2 é o valor de credito que vc ainda possui:
    dados[2] = credito - valor
    
    # retorna a lista:
    return dados
    

####################################################################################

# IMPORTANTE:

# função para descobrir se o que foi digitado é um numero:
def converter (valor):
    # declara a variavel retorno:
    retorno = None
    
    # Vai tentar converter o valor passado para float:
    try:
        retorno = float(valor)
    
    # se nao der certo retorna 0:
    except:
        print("O valor inserido anteriormente nao é um numero!!!!!")
        return 0
    
    return retorno



####################################################################################

# Dicionario das variaveis da pessoa:
Pessoa = {
    
    "Nome" : "",
    "Salario" : 0,
    "Menu" : 0,
    "opcoes" : []
    
}

# Dicionario das variaveis que seram usadas na conta:
Dados = {
    
    "Saldo" : 5000,
    "Credito" : 0,
    "CreditoPagar" : 0,
    "AuxiliarRetirar" : 0,
    "AuxiliarColocar" : 0,
    "Historico" : [],
    "Menu" : 0,
    
}

# ---------- Cadastro da pessoa ---------- :


# ---------- Controle da conta ---------- :

print("\n---------- Cadastrar ---------")

# Vai pedir o seu nome:
Pessoa["Nome"] = input("Digite o seu nome: ")

# Vai forçar vc a digitar um salario maior que 0:
while Pessoa["Salario"] <= 0:
    # Pede para digitar o salario, e chama a funçao que retorna o valor em float se possivel_
    # Caso nao seja um numero retorna o valor 0, entao volta a pedir o salario:
    Pessoa["Salario"] = converter(input("Digite o seu salario: "))

# Chama a funçao que descobre os creditos que vc tem direito:
Pessoa["opcoes"] = SeuCredito(Pessoa["Salario"])

# Força o usuario a escolher uma das 3 opçoes:
while (Pessoa["Menu"] < 1) or (Pessoa["Menu"] > 3) :
    
    print("\nBaseado em seu salario você tem direito a creditos de: \n")
    print(" 1 - " + str(Pessoa["opcoes"][0]))
    print(" 2 - " + str(Pessoa["opcoes"][1]))
    print(" 3 - " + str(Pessoa["opcoes"][2]))
    
    # pergunta a sua escolha e chama a funçao converter que retorna o valor em float_
    # Caso nao seja possivel retorna 0 e volta o laço do começo:
    Pessoa["Menu"] = converter(input("Qual das opções acima você deseja?"))
    
    # 50%
    if Pessoa["Menu"] == 1:
        Dados["Credito"] = Pessoa["opcoes"][0]
    
    # 75%
    elif(Pessoa["Menu"] == 2):
        Dados["Credito"] = Pessoa["opcoes"][1]
    
    # 100%
    elif(Pessoa["Menu"] == 3):
        Dados["Credito"] = Pessoa["opcoes"][2]
        
    else:
        print("Opção invalida!!!!")
        
# --------- Fim do Cadastro da pessoa --------- :
      
print("\nBem vindo: \n\n")

while (Dados["Menu"] != 5):
    
    valores = []
    
    # Cria um Menu
    print("\n--------- MENU ---------")
    print("\n 1 - Retirar\n 2 - Colocar\n 3 - Credito\n 4 - Extrato\n 5 - Sair\n")
    print("--------- MENU ---------\n")

    # Pergunta qual a escolha do usuario:
    Dados["Menu"] = 0
    Dados["Menu"] = converter(input("Qual a sua escolha?"))

    
    # Opção numero 1 é retirar:
    if (Dados["Menu"] == 1):  
        # Pede para o usuario digitar o valor que deseja retirar:
        Dados["AuxiliarRetirar"] = input("Digite o valor que deseja retirar: ")
        # Chama a função que converte o valor:
        Dados["AuxiliarRetirar"] = converter(Dados["AuxiliarRetirar"])
        # Chama a função para retirar o valor da conta:
        Dados["Saldo"] = Retirar(Dados["AuxiliarRetirar"], Dados["Saldo"])
        # Adiciona no historico:
        Dados["Historico"].append(Historico("Retirado", Dados["AuxiliarRetirar"]))

        
    # opção numero 2 é inserir:
    elif(Dados["Menu"] == 2):
        # Pede para o usuario digitar o valor que deseja inserir:
        Dados["AuxiliarColocar"] = input("Digite o valor que deseja inserir: ")
        # Chama a função que converte o valor:
        Dados["AuxiliarColocar"] = converter(Dados["AuxiliarColocar"])    
        # Chama a função para inserir o valor na conta:
        Dados["Saldo"] = Adicionar(Dados["AuxiliarColocar"], Dados["Saldo"])    
        # Adiciona no historico:
        Dados["Historico"].append(Historico("Adicionado", Dados["AuxiliarColocar"]))    

        
    # opção numero 3 é credito:    
    elif(Dados["Menu"] == 3):
        # Pede para o usuario digitar o valor que deseja inserir:
        Dados["AuxiliarColocar"] = input("Digite o valor que deseja de credito: ")
        # Chama a função que converte o valor:
        Dados["AuxiliarColocar"] = converter(Dados["AuxiliarColocar"])
        # Chama a função que calcula o credito e retorna um vetor:
        valores = Credito(Dados["AuxiliarColocar"], Dados["Credito"], Dados["Saldo"], Dados["CreditoPagar"])
        # Adiciona no saldo o valor que foi pedido:
        Dados["Saldo"] = Dados["Saldo"] + valores[0]
        # Adiciona no credito a pagar o valor que foi pedido:
        Dados["CreditoPagar"] = Dados["CreditoPagar"] + valores[1]
        # Diminui o credito a recuperar:
        Dados["Credito"] = Dados["Credito"] - valores[2]
        # Coloca no historico:
        Dados["Historico"].append(Historico("adicionado um credito em", valores[0]))    
     
    
    elif(Dados["Menu"] == 4):
        Extrato(Dados, Pessoa["Nome"])

    elif(Dados["Menu"] == 5):
        print("Saindo...")
        Dados["Verificador"] = False

    else:
        print("Opção invalida!!!!")
