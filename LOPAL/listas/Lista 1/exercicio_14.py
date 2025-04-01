#-*- coding: UTF-8 -*-

print('Ola usuario,o comerciante de um produto, e quis vender com um lucro de 45% se o valor da compra for menor que R$ 20,00; ou seja, ao contrario, o lucro será de 30%.')
produto = float(input("Me de o valor do produto"))
if produto < 20:
    lucro = produto * 45 / 100
    print("O valor do produto de 45% é de", lucro)
else:
    lucro = produto * 30 / 100
    print("O valor do produto de 30% é de", lucro)
