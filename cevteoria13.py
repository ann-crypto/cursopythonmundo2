for c in range(1, 6): #aqui ele começa a contar do 1 ao 5
    print('Oi')
print('FIM')

for g in range(0, 6): #aqui ele começa a contar do 1 ao 6
    print('Oi')
    print('FIM')

for a in range(6, 0, -1): #contar para trás
    print(a)

n = int(input('Digite um número: '))
for b in range(0, n+1): print(b)
print('FIM')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for m in range(inicio, fim+1, passo):
    print(m)
print('FIM')

s = 0
for y in range(0, 3):
    j = int(input('Digite um valor: '))
    s += j
print('O somatório de todos os valores foi {}.'.format(s))
