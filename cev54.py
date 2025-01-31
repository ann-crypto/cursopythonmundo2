from datetime import date
'''Crie um programa que leia o ano de nascimento de 7 pessoas. No final mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
totmaior = 0
totmenor = 0
for count in range (1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(count)))
    if date.today().year - ano >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
