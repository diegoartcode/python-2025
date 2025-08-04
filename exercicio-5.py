# Exercício:
# O programa recebe o valor de compra e se o cliente for um cliente frequente (responda com "sim" ou "não")
# O cliente recebe desconto se suas compras forem maiores que 1000 'ou' se for cliente frequente
## temos que tratar o valor de entrada "sim" ou "não" com .strip().lower()
# utilize a conditional if e else

# valor_compra = float(input('Digite o valor da compra: '))
# cliente_frequente = input('Você é um cliente frequente: (sim / não)').strip().lower()

# if valor_compra > 0:
#     if valor_compra > 1000 or cliente_frequente == 'sim':
#         print('Você recebeu um desconto')
#     else:
#         print('Voce não recebeu um desconto')
# else:
#     print('Valor da comprar invalido')

###################################################

# valor_compra = float(input('Digite o valor da compra: '))
# cliente_frequente = input('Você é um cliente frequente: (sim / não)')
# cliente_frequente_verificar = (cliente_frequente.strip().lower() == 'sim')

# if valor_compra > 1000 or cliente_frequente_verificar:
#     print('Você recebeu um desconto')
# else:
#     print('Voce não recebeu um desconto')

 
#Exercício:
# Escreva um programa que solicite ao usuário um número e verifique se o número é positivo ou negativo. Se o número for zero, informe que é zero.
# numero > 0: "O número é positivo."
# numero < 0: "O número é negativo."
# numero == 0: "O número é zero."

# numero = float(input('Digite um numero'))

# if numero > 0:
#     print('O número é positivo.')

# elif numero < 0:
#     print('O número é negativo.')
# else:
#     print('O número é zero.')

# num1 = float(input("Digite um numero: ")) 
# if num1 > 0:
#     print("positivo")
# elif num1 == 0:
#     print("zero")
# else:
#     print("negativo")
 
# Exercício:
# Peça ao usuário para inserir um número inteiro e verifique se é par ou ímpar. Exiba o resultado.

numero = int(input('Digite um numero inteiro'))
# print(numero % 2)
if numero % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')
 