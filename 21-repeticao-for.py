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


lista_nomes = ['Diego','Jhenny', 'Romeu','Julieta','João', 'Maria']
c = 0
for nome in lista_nomes:
    print(nome)
    c += 1 #c = c + 1
    print(c, nome)
