# -*- coding: UTF-8 -*-

print("Ola usuario, se o numero for de 123, o resultado devera ser 1*2*2=6, caso o numero seja negativo ou zero, a funçao deve retornar com uma mensagem")
num1=int(input("Digite o valor:"))
acum= 1

def calculo_de_produto(num1):
    global acum
    for i in range(num1-1,0,-1):
        if num1 % i == 0:
            acum = acum * i
    if num1 == acum:
        print("número otimo!")
    else:
        print("número nao muito bom!")
calculo_de_produto(num1)


