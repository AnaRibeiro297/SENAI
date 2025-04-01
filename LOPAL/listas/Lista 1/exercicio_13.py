#-*- coding: UTF-8 -*-

print('Ola Usuário, me de três notas e sua média e  depois eu vou lhe dizer e  analisar sua situação.')
nota1= float(input("Digite a primeira nota"))
nota2= float(input("Digite a segunda nota"))
nota3= float(input("Digite a terceira nota"))
falta= int(input("Digite a quantidade de faltas"))
media= (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Você esta aprovado")
elif media < 3 or falta > 20:
    print("Você esta reprovado")
else:
    print("Você esta de recuperação")
