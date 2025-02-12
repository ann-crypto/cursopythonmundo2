'''Crie um programa que leia o nome e o preço de váriso produtos. O programa deverá perguntar
se o usuário vai continuar. No final mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de r$ 1000
c) qual é o nome do produto mais barato'''

print('='*9)
print('LOJA ASR')
print('='*9)

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço > menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi: R$ {total:.2f}')
print(f'temos {totmil} produtos custando mais de R$ {1000}')
print(f'O produto mais barato foi {barato} que custa: R${menor:.2f}')
