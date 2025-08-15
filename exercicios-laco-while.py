# Exercício 1: Contagem de 1 a 10
# Imprima os números de 1 a 10.

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

#########################################################################
 
# Exercício 2: Soma dos Números
# Calcule a soma dos números de 1 a 100.

# i = 1
# soma = 0
# while i <= 100:
#     soma += i
#     i += 1
# print(soma)

#########################################################################
 
# Exercício 3: Tabuada do 5
# Imprima a tabuada do 5.

# i = 0
# while i <= 10:
#     tabuada = 5 * i
#     print(f'5 x {i} = {tabuada}')
#     i += 1
 
#########################################################################
 
# Exercício 4: Números Pares
# Imprima todos os números pares de 1 a 20.

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

#########################################################################
 
# Exercício 5: Quadrados dos Números
# Imprima os quadrados dos números de 1 a 10.

# i = 1 
# while i <= 10:
#     calculo = i ** 2
#     print(f'{i}^2 = {calculo}')
#     i += 1

#########################################################################
 
# Exercício 6: Contagem Regressiva
# Imprima uma contagem regressiva de 10 a 1.

# i = 10
# while i > 0:
#     print(i)
#     i -= 1 # i = i - 1

#########################################################################
 
# Exercício 7: Fatorial de um Número
# Calcule e imprima o fatorial do número 5.
 
# fatorial = 1
# i = 1
# numero = 10
# while i <= numero:
#     fatorial *= i # fatorial = fatorial * i
#     i += 1
# print(f'Fatorial de { numero} = {fatorial}')

#########################################################################
 
# Exercício 8: Números Ímpares
# Imprima todos os números ímpares de 1 a 20.
 
# i = 1
# while i <= 20:
#     if i % 2 != 0:
#         print(i)
#     i += 1 
#########################################################################
 
# Exercício 9: Contar Vogais
# Conte e imprima o número de vogais em uma string.
# string = "Hello, World!"
# vogais = "aeiouAEIOU"


# string = "Hello, World!"
# vogais = "aeiouAEIOU"
# contador = 0
# indice = 0
# # print(string[12])
# while indice < len(string):
#     if string[indice] in vogais:
#         contador += 1
#     indice += 1
# print(contador)

 
#########################################################################
 
# Exercício 10: Gerenciador de Lista de Compras
# Peça ao usuário para adicionar itens à sua lista de compras até que ele digite "sair".
# Inicializa a lista de compras vazia
# Loop para adicionar itens
# Exibe a lista de compras com o loop FOR

lista_compras = []

while True:
    item = input('Digite um item para a lista de compras (ou "Sair" para finalizar): ')
    if item.upper() == "SAIR":
        break
    lista_compras.append(item)
    print(lista_compras)

for i, item in enumerate(lista_compras, start=1):
    print(f'{i}: {item}')
   