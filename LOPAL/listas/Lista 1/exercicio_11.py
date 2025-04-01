#-*- coding: UTF-8 -*-

print("Ola usuario, me diga as suas duas notas, e lhe direi se você está aprovada, reprovado ou esta de recuperação")

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

soma = n1 + n2

if soma >= 7:
    print("Você foi aprovado!")

elif soma <= 3:
    print("Você foi reprovado")
   
else:
    print("Você está de recuperação")



