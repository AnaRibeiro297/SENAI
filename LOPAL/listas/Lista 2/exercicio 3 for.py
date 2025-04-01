# -*- coding: UTF-8 -*-

print("Ola usuario, me de uma valor que eu vou fazer o fatorial desse numero :C")

num1 = int(input("Digite um valor"))
f = 1

for x in range (1,num1 + 1):
    f = x * f
print("O resultado foi de: ", f)
