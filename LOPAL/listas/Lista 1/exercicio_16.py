#-*- coding: UTF-8 -*-


print('Ola usuario, me diz a sua idade, e vou lhe classificar a sua faixa etária')
idade = int(input("Digite a sua idade"))  
if idade <= 2:
    print("Você é um bebe")
elif idade > 2 and idade <= 12:
    print("Você é uma crianca")
elif idade > 12 and idade <= 23:
    print("Você é um adolescente")
elif idade > 23 and idade <= 70:
    print("Você é um adulto")
else:
    print("Você é um idoso")
