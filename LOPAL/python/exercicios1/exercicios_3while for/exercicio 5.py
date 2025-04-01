# -*- coding: UTF-8 -*-

print("Ola usuario, me de o sexo de várias pessoas e imprimir quantas pessoas são do sexo masculino")

cont= 0 

for i in range (10):
    s= str (input("Digite os sexo das pessoas: "))
    if s== "m" or s== "M":
        cont= cont + 1
print("A quantidade dos sexo sao de: ", cont)
