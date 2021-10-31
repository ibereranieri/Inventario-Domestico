#from tkinter import * #Biblioteca para interface grafica
#raiz=Tk()
#raiz.title("Janela de Entrada")
#raiz.geometry("650x320")
#raiz.mainloop()
#bibliotecas
import datetime #biblioteca utilizada para manipulaçao de data_da_compra
import os #comandos do sistema operacional
from pyfiglet import Figlet


#declaracao de variaveis
mercadoria="Nome da mercadoria"
data_da_compra=datetime.datetime(2021,10,31,0,0)
quantidade=0
codigodebarra=0
menu=0
m=0



def menu_inicial():
    custom_fig = Figlet(font='big')
    print(custom_fig.renderText('Sistema de Invetario Domestico'))
    print("Esse são os primeiros códigos do programa de inventario domestico")
    print("Selecione uma das opções do menu abaixo")
    print("1 - Entrada")
    print("2 - Saida")
    print("99 - Sair do programa")
    menu=int(input("Digite a opção desejada: "))
    return menu

menu=menu_inicial()
if menu==1:
    #os.system('cls') or None
    print("Você selecionou a opção de entrada de Produtos")
elif menu==2:
    #os.system('cls') or None
    print("Você selecionou a opção de saida de Produto")
elif menu==99:
    #os.system('cls') or None
    print("Você está abandonando o sistema")
else:
    #os.system('cls') or None
    print("fim de execucao")
    menu=menu_inicial()
