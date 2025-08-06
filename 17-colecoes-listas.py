#            0        1       2       3
pessoas = ['Diego','Jhenny','Nina','Celeste']
print(pessoas[1])

pessoas2 = ['Diego', 33]
nome, idade = pessoas2

print(pessoas2[0])
print(nome)

print(type(pessoas)) # retorna o tipo 

print(pessoas[3]) # retorna um indice

print(pessoas[-2]) # retorna um indice de traz para frente

print(pessoas[1:]) # retorna apartir do indice
print(pessoas[:3]) # retorna apartir do indice
# ['Diego','Jhenny','Nina','Celeste']
print(pessoas[1:3]) # retorna a parti do indice 1 até o 4, excluido o 3,4 

pessoas[3] = 'Pedro'

print(pessoas)

pessoas.extend(['João', 'Maria', 'Romeu', 'Julieta','João']) # função .extend inclui outra lista na lista atual 

print(pessoas)

pessoas.append('Ana') #inclui um registro no final da lista

print(pessoas)

pessoas.insert(2, 'Lucy') # inclui um registro, no local indicado
# primeiro argumento = indice
# segundo argumento = registro (dado)

print(pessoas)

pessoas.pop() # exclui o ultimo registro
print(pessoas)

pessoas.pop(4) # excluir o registro com o indice passado
print(pessoas)

pessoas.remove('Romeu') # exclui pelo registro passado
print(pessoas)

# pessoas.clear() # limpa toda a lista 
# print(pessoas)

print(pessoas.index('João')) # retorna em qual indice o registro está (sendo o primeiro registro encontrado)

print(pessoas.count('Maria')) # conta quantos registros tem passado pelo argumento
print(pessoas.count('João'))

pessoas.sort() # função .sort() ordena a lista em ordem ascendente 
print(pessoas)

numeros = [33,25,60,10,20]

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(maior_numero)
print(menor_numero)

turma = [
    ['João', 20, 'Desenvolvedor web'],
    ['Maria', 19, 'Desenvolvedora Python'],
    ['Romeu', 32, 'Desenvolvedor PHP'],
    ['Julieta', 31, 'Desenvolvedora Flutter']
]

print(turma[2][0]) # linha | coluna
print(f'Idade {turma[3][1]} de {turma[3][0]}') # linha | coluna

