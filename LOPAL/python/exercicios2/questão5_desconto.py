#-*- coding: UTF-8 -*-

print("Me diga qual preço da mercadoria e a porcentagem de desconto dela que eu lhe direi qual o desconto e o preço a pagar")
num1= float(input("Preço da mercadoria: "))
num2= float(input("porcentagemde desconto: "))

desconto= num1/100 * num2
print("O valor do desconto é de: ",num2, "E o valor com o desconto é de: ",desconto)

