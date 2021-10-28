import tkinter as tk
import tkinter.font as tkFont
from functools import partial

###################################################################################################################

def converter (valor):
    # declara a variavel retorno:
    retorno = None
    
    # Vai tentar converter o valor passado para float:
    try:
        retorno = float(valor)
    
    # se nao der certo retorna 0:
    except:
        # print("O valor inserido anteriormente nao é um numero!!!!!")
        return 0
    
    return retorno

###################################################################################################################

# ----- criando menu da base de dados:
def baseDados( dados = []):
    
    # criando tela:
    baseDados = tk.Tk()
    baseDados.geometry("400x400")
    
    # criando label:
    LblBaseDados = tk.Label(baseDados, text = "Base de dados", font = TituloStyle)
    LblBaseDados.place(relwidth = 0.5, relheight = 0.05, relx = 0.25, rely = 0.025)

    # criando lista:
    DadosLista = tk.Listbox(baseDados)
    DadosLista.place(relwidth = 0.970, relheight = 0.40, relx = 0.01, rely = 0.075)
    
    # colocando os dados na lista:
    for item in dados:
        DadosLista.insert(0, item)
    
    # criando caixa de texto:
    EntradaDados = tk.Entry()
    EntradaDados.place(relwidth = 0.2, relheight = 0.2, relx = 0.01, rely = 0.50)
        
    # criando botoes:
    #BtnAdd = tk.Button(baseDados, text = "Adicionar", width = "17", height = "2", command = partial(baseDados, 0))
    #BtnAdd.place(relwidth = 0.2, relheight = 0.2, relx = 0.01, rely = 0.50)
    
    baseDados.mainloop()  

# funções para base de dados:
def addBaseDados(num):
    coment = inputcoment.get()
    comentsList.insert(0, coment)
    
###################################################################################################################

# ----- Declaração de variaveis:
Amostra = [15,25,50,25,300,15,25,50,25,300,15,25,50,25,300] 



###################################################################################################################

# ----- Criando tela principal:

TelaPrincipal = tk.Tk()
TelaPrincipal.geometry("550x500")
TelaPrincipal.title("Oficina Python")


###################################################################################################################

# ----- criando grupo do menu:

# criando menu:
Menu = tk.LabelFrame(TelaPrincipal)

# posicionando menu:
Menu.place(relwidth = 0.20, relheight = 1)


# Botão base de dados:
BtnBaseDados = tk.Button(Menu, text = "Base de Dados", width = "17", height = "2", command = partial(baseDados, Amostra))
BtnBaseDados.place(relwidth = 0.90, relheight = 0.12, relx = 0.05, rely = 0.005)

###################################################################################################################

# ------ Criando titulo:
Titulo = tk.LabelFrame(TelaPrincipal)
Titulo.place(relwidth = 0.80, relheight = 0.20, relx = 0.20)

# ----- Label do titulo:

# Criando estilo da letra:
TituloStyle = tkFont.Font(family="Lucida Grande", size = 20)

# criando label:
LblTitulo = tk.Label(Titulo, text = "", font = TituloStyle)
LblTitulo.place(relwidth = 1, relheight = 1)

###################################################################################################################

# rodando...
TelaPrincipal.mainloop()
