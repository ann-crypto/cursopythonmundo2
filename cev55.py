'''Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor
peso lidos.'''
maior = 0
menor = 0
for count in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(count)))
    if count == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {} Kg.'.format(maior))
print('O menor peso lido foi {} Kg.'.format(menor))
