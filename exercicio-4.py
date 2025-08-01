
nota1 = int(input('Digite a primeira nota (0 a 10): '))
nota2 = int(input('Digite a segunda nota (0 a 10): '))
nota3 = int(input('Digite a terceira nota (0 a 10): '))



if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10  :
    media = (nota1 + nota2 + nota3) / 3
    print(f'Calculo da media {media:.2f}')
    if media >= 7:
        print("Aprovado!")
    elif media >= 5:
        print("Recuperação!")
    else:
        print('Reprovado!')
else:
    print('Digite as notas de 0 a 10')
    




