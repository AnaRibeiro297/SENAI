# -*- coding: UTF-8 -*-
 
r = 0
a = 0
r = float(input("Digite o raio do seu circulo"))
a = float(input("Digite a altura do seu circulo"))
resultado_r = r * r
pi = 3.14
def volume (resultado_r, a, pi):
    return ( resultado_r * a * pi)

total = (volume(resultado_r, a, pi))
print (f"O valor total é: {total:.2f}")
