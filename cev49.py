'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
so que agora utilizando um laço for.'''

num = int(input('Digite um número para saber sua tabuada: '))
print('*' * 11)
for tabuada in range(1, 11):
    print(f'{num} x {tabuada} = {num * tabuada}')
print('*' * 11)
