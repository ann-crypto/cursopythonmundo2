'''Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F',.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0] #primeira letra, fatiamento
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor, informe seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
