# solicite para o usuario 3 notas de (0 a 10).
# calcule a média das três notas e com base na média, exiba a situação do aluno

# se a média for maior ou igual a 7, exiba: "Aprovado!"
# se a média for maior ou igual a 5, exiba: "Recuperação!"
# se a média for menor que 5, exiba: "Reprovado!"


# Solicite as 3 notas do aluno

nota1 = int(input('Digite a primeira nota (0 a 10): '))
nota2 = int(input('Digite a segunda nota (0 a 10): '))
nota3 = int(input('Digite a terceira nota (0 a 10): '))


# Calcular a média
media = (nota1 + nota2 + nota3) / 3


# Exibir a média formatada com 2 casas decimais

print(f'Calculo da media {media:.2f}')


# verifica a situação com if / elif / else

if media >= 7:
    print("Aprovado!")
elif media >= 5:
    print("Recuperação!")
else:
    print('Reprovado!')

# se a média for maior ou igual a 7, exiba: "Aprovado!"
# se a média for maior ou igual a 5, exiba: "Recuperação!"
# se a média for menor que 5, exiba: "Reprovado!"