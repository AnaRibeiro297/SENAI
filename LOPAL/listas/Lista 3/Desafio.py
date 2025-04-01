# -*- coding: UTF-8 -*-

print("Ola usuario, me da um numero e vou lhe dizer a quantidade de digitos que ele tem")

n1 = int(input("Me da um numero"))
contagem = 0
def cont (n1):
    global contagem
    while n1 >=1:
        n1 = n1 / 10
        contagem +=1
cont(n1)
print("O numero digitados é igual a: ", contagem)
