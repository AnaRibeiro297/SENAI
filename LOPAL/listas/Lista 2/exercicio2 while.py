#-*- coding: UTF-8 -*-

print("Ola usuario, me de os valores e eu vou e lhe imprimir o maior e o menor numero")

n1 = float(input("Digite um valor"))
maior = n1
menor = n1

while n1 >= 0:
    n1 = float(input("Digite um valor"))
    if n1 < 0:
        break
    elif n1 < menor:
        menor = n1
    elif n1 > maior:
        maior = n1
print("O maior valor é de: ",maior)
print("O menor valor é de: ",menor)
    

