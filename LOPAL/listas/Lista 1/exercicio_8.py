#-*- coding: UTF-8 -*-

print("Ola usuario, a prefeitura de Contagem abriu uma linha de crédito para os funcionários estatutários, e O valor máximo da prestação não poderá ultrapassar 30% do salário bruto")

n1= float(input("Digite o valor do salario: "))
n2= int(input("Digite o valor da prestação: "))

sal_porc= (n1*30)/100

if n2>sal_porc:
    print("O valor maximo nao podera ser concebido")
else:
    print("O valor maximo podera ser concebido")
