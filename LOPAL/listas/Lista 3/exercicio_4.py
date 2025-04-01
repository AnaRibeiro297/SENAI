-*- coding: UTF-8 -*-

print("Ola usuari#o, me de uma função que imprima a contagem regressiva ate o zero, e vou lhe dizer cada numero ele deve ser impresso")
num1 = int(input("Digite um numero!"))
def contagem_regressiva(num1): 
  for i in range(num1, 0,-1):
        print(i)
contagem_regressiva(num1)
print("Parabéns, Feliz ano novo")
