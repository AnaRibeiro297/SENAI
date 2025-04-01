# -*- coding: UTF-8 -*-

cont = 0
acum = 0

while True:
    valor = float(input("Digite os valores e no final lhe darei a media: "))
    if valor < 0:
        print("Você quis sair")
        break
    acum = acum + valor
    cont = cont + 1
    media = acum / cont

print("A media dos numeros digitado é de: " , media)
    
