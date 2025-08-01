
nota1 = int(input('Digite a primeira nota (0 a 10): '))
nota2 = int(input('Digite a segunda nota (0 a 10): '))
nota3 = int(input('Digite a terceira nota (0 a 10): '))



nota1_verificada = nota1 >= 0 and nota1 <= 10
nota2_verificada = nota2 >= 0 and nota2 <= 10
nota3_verificada = nota3 >= 0 and nota3 <= 10

if nota1_verificada == True and nota2_verificada == True and nota3_verificada == True:
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
    




