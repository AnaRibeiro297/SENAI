# -*- coding: UTF-8 -*-

print("Ola usuario, imforma quantos numeros entre 100 e 200 foram digitados, e quando o valor de 0 for lido, o programa devera ser executado")

x = 0

while True:
    valor = float(input("Digite o seu valor: "))
    if valor == 0:
        break
    if valor >=100 and valor <=200:
        x = x + 1
print("A contagem ficou em: ", x)
    
