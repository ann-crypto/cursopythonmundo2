'''Crie um progrma que leia duas notas de um aluno e calcule sua média, mostrando
uma mensagem no final, de acordo com a média atingida
media abaixo de 5.0 REPROVADO
media entre 5.0 e 6.9 RECUPERAÇÃO
media 7.0 ou superior
APROVADO'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}.'.format(nota1, nota2, media,))
if media < 5.0:
    print('O aluno está REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está APROVADO!')
