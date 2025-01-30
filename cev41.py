from datetime import date
'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade
até 9 anos: mirim
até 14 anos: infantil
até 19 anos: junior
até 20 anos senior
acima: master'''

print('-=' * 17)
print('Confederação Nacional de Natação!')
print('-=' * 17)
ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('A categoria é: MIRIM')
elif idade <= 14:
    print('A categoria é: INFANTIL')
elif idade <= 19:
    (print('A categoria é: JUNIOR'))
elif idade <= 25:
    (print('A categoria é: SENIOR'))
else:
    print('A categoria é: MASTER')
