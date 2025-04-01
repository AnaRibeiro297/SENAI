# -*- coding: UTF-8 -*-

print("Ola usuario, eu vou lhe apresentar os numeros divisores")

valor1 = int(input("digite um número"))
for v in range(1, valor1, +1):
    if valor1 % v == 0:
        print (v)
        
