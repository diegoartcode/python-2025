# Exercício: Criar um Conjunto
# Criando um conjunto chamado frutas = "maçã", "banana", "laranja"
# Saida Conjunto de frutas: [frutas]

# frutas = {"maçã", "banana", "laranja"}
# print(frutas)

# #############################################
 
# Exercício: Adicionar Elementos ao Conjunto
# Saida: Conjunto de frutas após adição: [frutas]
 
# frutas = {"maçã", "banana", "laranja"}
# print(frutas)
# frutas.add('uva')
# print(frutas)
 
##########################################################
 
# Exercício: Remover Elementos do Conjunto
# Removendo uma fruta do conjunto usando remove
# Saida: Conjunto de frutas após remoção: [frutas]


# frutas = {"maçã", "banana", "laranja"}
# print(frutas)
# # frutas.add('uva')
# frutas.remove('uva')
# print(frutas)

###############################################################
 
# Exercício: Verificar a Existência de um Elemento
# Verificando se a fruta 'laranja' está no conjunto
# Use a condicional if e else
# Saida verdadeira A fruta 'laranja' está no conjunto.
# Saida Falsa A fruta 'laranja' não está no conjunto.

# frutas = {"maçã", "banana", "laranja"} 
# fruta = input('Digite uma fruta: ')

# if fruta in frutas:
#     print(f'A fruta {fruta} esta no conjunto')
# else:
#     print(f'A fruta {fruta} não esta no conjunto')
###########################################
 
# Exercício: Operações de União
# Criando outro conjunto de frutas 
# frutas_citricas = "laranja", "limão", "tangerina"
# Saida: Todas as frutas: [todas_as_frutas]
# frutas = {"maçã", "banana", "laranja"}  
# frutas_citricas = {"laranja", "limão", "tangerina"} 
# todas_as_frutas = frutas.union(frutas_citricas)
# print(todas_as_frutas)
###########################################
 
# Exercício: Operações de Interseção
# Criando um conjunto de frutas tropicais
# frutas_tropicais = "maçã", "banana", "coco"
# Encontrando a interseção entre os dois conjuntos usando .intersection 
# Saida Frutas comuns: [frutas_comuns]

# frutas = {"maçã", "coco", "banana", "laranja"}
# frutas_tropicais = {"maçã", "banana", "coco"}
# frutas_comuns = frutas.intersection(frutas_tropicais)
# print(frutas_comuns)

#####################################################
 
# Exercício: Diferença de Conjuntos
# Crie um conjunto de frutas de inverno
# frutas_inverno = "kiwi", "maçã", "pêra"
# Encontrando a diferença entre 'frutas' e 'frutas_inverno' usando .difference
# Saida Frutas que não estão no inverno: [frutas_diferentes]

# frutas = {"maçã", "coco", "banana", "laranja"}
# frutas_inverno = {"kiwi", "maçã", "pêra"}
# frutas_diferentes = frutas.difference(frutas_inverno)
# print(frutas_diferentes)
# frutas_diferentes1 = frutas_inverno.difference(frutas)
# print(frutas_diferentes1)






######################################################################
 
# Exercício: Conjunto de Elementos Únicos
# Crie uma lista com frutas repetidas
# lista_frutas = "maçã", "banana", "laranja", "maçã", "uva", "banana"
# Convertendo a lista em um conjunto para obter elementos únicos, usando o set()
# Saida: Frutas únicas: [frutas_unicas]
 
# lista_frutas = ["maçã", "banana", "laranja", "maçã", "uva", "banana"]

# print(lista_frutas)

# frutas_unicas = set(lista_frutas)
# print(frutas_unicas)
################################################################
 
# Exercício: Tamanho do Conjunto
# Crie um conjunto frutas "maçã", "banana", "laranja", "maçã", "uva"
# Obtendo o tamanho do conjunto de frutas, usando o len()
# Saida: O tamanho do conjunto de frutas é: [tamanho_frutas]

# frutas = {"maçã", "banana", "laranja", "maçã", "uva"}
# tamanho_conjunto_frutas = len(frutas)
# print(tamanho_conjunto_frutas)
 
##############################################################
 
# Exercício: Limpar um Conjunto
# Crie um conjunto frutas "maçã", "banana", "laranja", "maçã", "uva" 
# Limpando todos os elementos do conjunto, usando .clear()
# Saida: Conjunto de frutas após limpeza: frutas

frutas = {"maçã", "banana", "laranja", "maçã", "uva" }
print(frutas)
frutas.clear()
print(frutas)