#1ªLista (exercício 1) - Aluno: Raphael Viana / Professor: Fernando Masanori
#3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
#Calcule o total em segundos.
dias = int(input('Digite a quantidade de dias:'))
horas = int(input('Digite a quantidade de horas:'))
minutos = int(input('Digite a quantidade de minutos:'))
segundos = int(input('Digite a quantidade de segundos:'))
contDias= (dias*24)
contHoras= ((contDias+horas)*60)
contMinutos= ((contHoras+minutos)*60)
contSegundos=(contMinutos+segundos)
print(contSegundos)