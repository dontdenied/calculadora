from funcoes import *

def menu():
    while True:
        print('1 - somar\n2 - subtrair\n3 - multiplicar\n4 - dividir\n5 - sair')
        escolha = input('~> ')
        if '12345' in escolha:
            if '1' in escolha[0]:
                somar()
            elif '2' in escolha[0]:
                subtrair()
            elif '3' in escolha[0]:
                multiplicar()
            elif '4' in escolha[0]:
                try:
                    dividir()
                except ZeroDivisionError as error:
                        continue
        elif 1 or 2 or 3 or 4 or 5 in escolha[0]:
            if 1 in escolha[0]:
                somar()
            elif 2 in escolha[0]:
                subtrair()
            elif 3 in escolha[0]:
                multiplicar()
            elif 4 in escolha[0]:
                try:
                    dividir()
                except ZeroDivisionError as error:
                        continue
        elif escolha[0] != 1 or escolha[0] != 2 or escolha[0] != 3 or escolha[0] != 4 or escolha[0] != 5:
             print('escolha indisponível, tente novamente')
             continue
        elif escolha[0] == 5:
             break
        else:
            print('escolha indisponível, tente novamente')
            continue
    
        