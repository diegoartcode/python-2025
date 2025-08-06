# set = conjunto

# set = funciona com uma lista desordenada
# Não aceita valores duplicados
# dados não podem ser alterados 
# podemos incluir e excluir dados

frutas = {'Maça', 'Laranja', 'Abacaxi','Maça'}
          
print(frutas)
print(type(frutas))

frutas.add('Uva')
print(frutas)

frutas.remove('Abacaxi')
print(frutas)

frutas.pop()
print(frutas)

outras_frutas = {'Pera','Banana'}

frutas.update(outras_frutas)
print(frutas)

frutas_citricas = {'Laranja', 'Limão', 'Tangerina','Limão'}

todas_frutas = frutas.union(frutas_citricas)
print(todas_frutas)

# print(frutas.intersection(todas_frutas)) # teste

grupo_a = {'Diego', 'Jhenny'}
grupo_b = {'João', 'Maria', 'Jhenny'}

# união
uniao = grupo_a | grupo_b
print(uniao)

# interseção
intersecao = grupo_a & grupo_b
print(intersecao)

# Diferancial
diferencial = grupo_a - grupo_b
print(diferencial)
