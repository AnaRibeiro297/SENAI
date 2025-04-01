#-*- coding: UTF-8 -*-

print("Ola usuario, me de os valores que eu lhe direi a soma e a média desses número")

n = float(input("Digite o numero"))
n2 = 0
n3 = 0
while n >= -1:
    print (n)
    n2 = n2 + 1
    media = n2
    n3 = n3 + n
    n = float(input("Digite um numero"))

    if n == 0:
        media = n2 + 1
        break
res = n3 / media
print(" A média dos numeros exibidos foi de", res)

