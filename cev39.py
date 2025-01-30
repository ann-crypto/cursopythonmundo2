from datetime import date
'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
se ele ainda vai se alistar ao serviço militar
se é a hora de se alistar
se já passou do tempo de alistamento
seu programa também deverá mostrar o tempo que falta ou o que passou do prazo'''

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('Quem nasceu em {} tem anos {} em {}'.format(ano, idade, date.today().year))

if idade < 18:
    print('Ainda faltam {} ano(s) para o alistamento\nseu alistamento será em {}'.format(18 - idade, date.today().year + 18 - idade))

elif idade == 18:
    print('Está na hora de se alistar')

else:
    print('Ja se passaram {} do tempo de alistamento'.format(idade - 18))
