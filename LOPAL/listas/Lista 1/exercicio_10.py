#-*- coding: UTF-8 -*-

print("Ola usuario, faça um algoritmo para ler três valores reais e informar se estes podem ou não formar, os lados de um triângulo e qual tipo de triângulo seria: equilátero, isósceles ou escaleno")

n1= float(input("Digite o seu primeiro valor: "))
n2= float(input("Digite o seu segundo valor: "))
n3= float(input("Digite o seu terceiro valor: "))

soma1 = n1 + n2
soma2 = n2 + n3
soma3 = n3 + n1


if soma1 < n3 or soma2 < n1 or soma3 < n2:
    print("O seu triângulo está errado")
elif n1 == n2 and n1 == n3 or n1 == n3 and n1 == n2 or n2 == n3 and n2 == n1:
    print("O seu  triângulo é isósceles")
elif n1 == n2 and n3 == n1:
    print("O seu triângulo é equilátero")
elif n1 == n2 and n3 != n1 and n2 != n3:
    print ("O seu triângulo é escaleno")

