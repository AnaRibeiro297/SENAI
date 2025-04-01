#-*- coding: UTF-8 -*-

print("Ola usuario, me de uma função de um numero fornecido que eu vou lhe dizer, tabela dever ir sa 1 até 10")

n1 = int(input("Digite um número inteiro para fazer uma tabela (de 1 à 10)"))
m = 1
def tabela(n, m):
    for multiplicaçao in range(1,11):
        print(f'{n} * { m} = {n1 * m}')
        m +=1
tabela(n1, m)
