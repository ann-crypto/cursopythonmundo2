'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
Primo: dividido apenas por 1 e ele mesmo.'''

num = int(input('Digite um número: '))
tot = 0
for count in range(1, num + 1):
    if num % count == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(count), end=' ')
print('\n\033[mO número {} foi divisível {} vezes!'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
