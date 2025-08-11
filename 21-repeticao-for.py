# 21-repeticao-for.py

#levantar
#sair da mesa
#dar 10 passos
#cheguei

# print('levantar')
# print('sair da mesa')
# print('Passo 1')
# print('Passo 2')
# print('Passo 3')
# print('Passo 4')
# print('Passo 5')
# print('Passo 6')
# print('Passo 7')
# print('Passo 8')
# print('Passo 9')
# print('Passo 10')
# print('cheguei')

# print('levantar')
# print('sair da mesa')
# for passo in range(10):
#     print(f'Passo{passo}')
# print('cheguei')

# print('levantar')
# print('sair da mesa')
# for passo in range(1,10+1):
#     print(f'Passo{passo}')
# print('cheguei')

# print('levantar')
# print('sair da mesa')
# for passo in range(0,10+1,2):
#     print(f'Passo{passo}')
# print('cheguei')


# numero = int(input('Digite um valor final: '))
# numero += 1 # numero = numero + 1

# print(numero)

# for i in range(0,numero, 3):
#     print(i)
# print(i)


# for i in range (20, 0-1, -2 ):
#     print(i)

###### exercicio
# quatro valores pelo usuario
# soma 
# resultado 
# soma = 0
# for i in range(1, 4 + 1):
#     # print(i)
#     numero = int(input(f'Digite um numero {i}: '))
#     # soma = soma + numero
#     soma += numero
#     # print(soma)
# print(soma)


lista_nomes = ['Diego','Jhenny', 'Romeu','Julieta','João', 'Maria','teste']
# c = 0
# for nome in lista_nomes:
#     print(nome)
#     c += 1 #c = c + 1
#     print(c, nome)

# print(len(lista_nomes))
# print(lista_nomes[0])

# for i in range(len(lista_nomes)):
#     print(i)
#     print(lista_nomes[i])

# lista_pessoas = []
# print(lista_pessoas)
# for i in range(0,2 + 1):
#     nome = input('Digite um nome: ') 
#     lista_pessoas.append(nome)
# print(lista_pessoas)

lista_produtos = {
    'Computador' : 4500.00,
    'Impressora' : 350.00,
    'Teclado' : 100.50
}
# print(lista_produtos['Teclado'])
# for produto, valor in lista_produtos.items():
#     print(produto)
#     print(valor)

# for produto in lista_produtos:
#     print(produto)
#     print(lista_produtos[produto])
#     print(f'Produto {produto} custa R${lista_produtos[produto]:.2f}')

for produto in lista_produtos.keys():
    print(produto)

for produto in lista_produtos.values():
    print(produto)
