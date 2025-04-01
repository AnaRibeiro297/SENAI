#-*- coding: UTF-8 -*-

print('Ola usuario, me de a temperatura atual, e vou dar a temperatura em Farenheit.')
temp = float(input("Digite a temperatura"))
if temp <= 15:
    print('Está muito frio')
elif temp >= 16 and temp <= 23:
    print('Está frio')
elif temp >= 24 and temp <= 26:
    print('Está agradável')
elif temp >= 26 and temp <= 30:
    print('Está quente')
elif temp >= 31:
    print('Está muito Quente')
