# -*- coding: UTF-8 -*-

print("ola usuario, me da dois numeros, e vou lhe dizer qual operação voce irá fazer e depois eu irei fazer a conta")


valor1 = int(input ("Digite o seu primeiro numero: "))
valor2 = int(input ("Digite o segundo numero: "))
op = input ("Me da uma opção de operação, e vou escolher qual função vou usar no numero que eu vou digitar e o resultado será o escolhido: + - / *: ")

def adiçao(valor1,valor2):
    adiçao = valor1 + valor2
    print(adiçao)

def subtraçao(valor1,valor2):
    subtraçao = valor1 - valor2
    print(subtraçao)
   
def divisao(valor1,valor2):
    divisao = valor1 / valor2
    print(divisao)

def multiplicaçao(valor1,valor2):
    multiplicaçao = valor1 * valor2
    print(multiplicaçao)


if op == '+':
    adiçao(valor1,valor2)

elif op == '-':
    subtraçao(valor1,valor2)

elif op == '/':
    divisao(valor1,valor2)

elif op == '*':
    multiplicaçao(valor1,valor2)

