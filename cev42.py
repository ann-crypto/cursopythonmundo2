'''Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo
de triangulo será formado
equilátero: todos os lados iguais
isósceles: dois lados iguais
escaleno: todos os lados diferentes'''

print('-*' * 12)
print('Analisador de Triângulos')
print('-*' * 12)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if a == b and b == c:
        print('EQUILATERO!')
    elif a != b and a != c:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
