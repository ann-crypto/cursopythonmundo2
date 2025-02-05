'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

'''n = s = 0
while n != 999: #utilizando o enquanto com flag
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s))'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') #python 3.6+
print('O {} tem {} anos.'.format(nome, idade)) #python 3
print(' %s tem %d anos.' % (nome, idade)) #python 2



