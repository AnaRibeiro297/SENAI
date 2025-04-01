#-*- coding: UTF-8 -*-
print("ola usuario, irei te informar o total de segundo com base na sua quantidade de dias, horas, minutos, segundos")
dias= int(input("digite sua quantidade de dias: "))
horas= int(input("digite sua horas: "))
minutos= int(input("digite os minutos: "))
segundos= int(input("digite seus segundos: "))

dia_pseg= dias * 24 * 60 * 60 * 60
horas_pseg= horas * 60 * 60
minutos_pseg= minutos * 60

soma= dia_pseg + horas_pseg + minutos_pseg + segundos
print("os resultados em segundos é de: ",soma)



