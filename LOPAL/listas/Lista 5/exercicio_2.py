# -*- coding: UTF-8 -*-

print("Ola usuario, me um vetor de 10 números reais e vou lhe mostrar em ordem inversa")

L = []
for e in range (10):
    x = int(input("Digite um valor: "))
    L.append (x)
    print (L[::-1])
print(L)
