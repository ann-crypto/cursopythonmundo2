'''Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritimetica.
No final mostre os 10 primeiros termos dessa progressão.'''

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for count in range (termo, decimo + razao, razao):
    print('{} -> '.format(count), end='')
print('ACABOU!')
