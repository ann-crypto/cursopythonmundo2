'''Refaça o desafio 51, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros
termos da progressão usando estrutura while'''

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
decimo = primeiro + (10 - 1) * razao
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('ACABOU!')
