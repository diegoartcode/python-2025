# Exercício 1: Contagem de 1 a 10
# Imprima os números de 1 a 10.
 
# for i in range(1,10+1):
#     print(i)

 
##########################################################################
 
# Exercício 2: Soma dos Números
# Calcule a soma dos números de 1 a 100.
# soma = 0 
# for i in range(1,100+1):
#     # print(i) 
#     soma += i #soma = soma + i
# print(soma)
 
##########################################################################
 
# Exercício 3: Lista de Nomes
# Crie uma lista de nomes e imprima cada um deles.
# nomes = ["Alice", "Bob", "Carlos"]
# nomes = ["Alice", "Bob", "Carlos"]

# for nome in nomes:
#     print(nome)

 
##########################################################################
 
# Exercício 4: Tabuada do 5
# Imprima a tabuada do 5.

# for i in range(10+1):
#     # print(i) 
#     tabuada = 5 * i
#     # print(tabuada)
#     print(f'5 x {i} = {tabuada}' )

# numero = int(input('Digite um numero: '))
# for i in range(10+1):
#     # print(i) 
#     tabuada = numero * i
#     # print(tabuada)
#     print(f'{numero} x {i} = {tabuada}' ) 
##########################################################################
 
# Exercício 5: Números Pares
# Imprima todos os números pares de 1 a 20.

# for i in range(2,20+1,2):
#     print(i) 

# for i in range(1,20+1):
#     if i % 2 == 0:
#         print(i)
 
##########################################################################
 
# Exercício 6: Quadrados dos Números
# Imprima os quadrados dos números de 1 a 10.

# for i in range(1,10+1):
#     calculo = i ** 2
#     # print(calculo)
#     print(f'{i}^2 = {calculo}')
 
##########################################################################
 
# Exercício 7: Contagem Regressiva
# Imprima uma contagem regressiva de 10 a 1.

# for i in range(10,0,-1):
#     print(i) 
##########################################################################
 
# Exercício 8: Fatorial de um Número
# Calcule e imprima o fatorial do número 5.
# 5!=5×4×3×2×1=120
# 5!=1×2×3×4×5=120

# fatorial = 1
# for i in range(1,5+1):
#     fatorial *= i #fatorial = fatorial * i
# # print(fatorial)
# print(f'Fatorial de 5 = {fatorial}')
 
##########################################################################
 
# Exercício 9: Números Ímpares
# Imprima todos os números ímpares de 1 a 20.

# for i in range(1,20+1):
#     if i % 2 != 0:
#         print(i)
 
##########################################################################
 
# Exercício 10: Contar Vogais
# crie duas variaveis pra realizar o exercício
# string = "Hello, World!"
# vogais = "aeiouAEIOU"
# Conte e imprima o número de vogais em uma string.

string = "Hello, World!"
vogais = "aeiouAEIOU"

contador = 0
for letra in string:
    # print(letra)
    if letra in vogais:
        # print(letra)
        contador += 1 # contador = contador + 1
print(contador) 