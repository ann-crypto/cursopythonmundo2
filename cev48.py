'''Faça um programa que calcule a soma de todos os números impáres que são múltiplos
de 3 e que se encontram no intervalo entre 1 até 500.'''

soma = 0
cont = 0
for lista in range (1,501, 2):
    if lista % 3 == 0:
        cont += 1
        soma += lista
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma, end= ' '))
print('FIM')
