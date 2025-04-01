# -*- coding: UTF-8 -*-

fim = int(input("Defina quantas vezes vai repetir: "))
x = 1
soma = 0
while x <= fim:
    n = int(input("%d Digite o número: " % x))
    soma = soma + n
    x = x + 1
print ("Média: %5.2f" % (soma/fim))
