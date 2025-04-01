#-*- coding: UTF-8 -*-

print("me de o numero de horas trabalhadas, a cada hora empresa vai pagar 19.50, e recolhedo-se para o importo de renda um valor de 10%, e a penas se for acima de R$1.500")

n1= int(input("Me de o total de hora  trabalhadas: "))

if n1>1.500:
     salario= n1*19.50
     imposto= salario*0.10
     resposta_final= salario-imposto
     print("O valor para receber é de: ",resposta_final)

else:
    salario= n1*19.50
print("o salario para receber é de: ")
