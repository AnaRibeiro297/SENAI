# -*- coding: UTF-8 -*-
print("Ola usuario, cria um contador, enquanto os numeros forem positivos e depois imprimir os numeros digitados")

x = 0
while True:
    num= float(input("Me da um valor: "))
    if num <=0:
        break
    if num > 0:
        x = x + 1
print("O valor da contagem foi: " , x)
    


