#-*- coding: UTF-8 -*-

print("Digite sua velocidade e eu lhe direi se você esta certo ou se foi multado, casa for, tambem direi o valor da multa")

vel= int(input("Digite a velocidade do carro"))
if vel < 80:
    print ("Você está livre")
else:
    print("Voce esta multado voce vai pagar R$" , (vel - 80) * 5)

        
        
