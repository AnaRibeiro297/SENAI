# -*- coding: UTF-8 -*-

print("ola usuario, entre com os números e imprimir o triplo de cada número. E o programa acaba quando entrar o número -999")

v = 0
while True:
    v = int(input("Digite um numero : "))
    if v == -999:
        break
    print (v*3)
print("O programa foi encerrado")
