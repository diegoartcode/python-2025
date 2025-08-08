# Exercício: Criar e Exibir uma Lista
# Crie uma lista chamada frutas que contenha pelo menos 5 tipos de frutas.
# frutas = "maçã", "banana", "laranja", "uva", "kiwi"
# Exiba a lista de frutas na tela.
# Saida: Lista de frutas: [frutas]

# frutas = ["maçã", "banana", "laranja", "uva", "kiwi"]
# print(f'Lista de frutas: {frutas[0]}, {frutas[1]} {frutas[2]}, {frutas[3]}, {frutas[4]}')
 
###########################################
# Exercício: Adicionar e Remover Elementos
# Adicione mais uma fruta à lista frutas criada no exercício anterior.
# Remova a primeira fruta da lista.
# Exiba a lista atualizada.
# Saida: Lista de frutas após adições e remoções: [frutas]

# frutas = ["maçã", "banana", "laranja", "uva", "kiwi"]
# frutas.append('Manga')
# print(frutas)
# frutas.pop(0)
# print(frutas) 

# print(f'Lista de frutas após adições e remoções: {frutas}')
#######################################################################
 
# Exercício: Ordenar a Lista
# Crie uma nova lista chamada numeros com os números: 3, 1, 4, 1, 5, 9, 2, 6, 5.
# Ordene a lista numeros em ordem crescente.
# Exiba a lista ordenada.
# Saida: Lista de números ordenada: [numeros]
# numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numeros)
# numeros.sort() 
# print(numeros)
#######################################################################
 
# Exercício: Fatiamento de Listas
# Usando a lista numeros do exercício anterior, exiba os três primeiros números da lista.
# Exiba os números do meio (ou seja, exclua os primeiros e os últimos dois).
# Exibindo os três primeiros números da lista 'numeros'
# Saida 1: Três primeiros números: [3, 1, 4]
# Saida 2: Números do meio: [4, 1, 5, 9, 2]
# numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# print(numeros[0],numeros[1],numeros[2])
# print(numeros[:3])

# print(numeros[2:-2])

#######################################################################
 
# Exercício: Encontrar o Maior e Menor Número
# Usando a lista numeros, encontre e exiba o maior e o menor número da lista.
# Encontrando o maior e o menor número na lista 'numeros'
# Saida 1:  Maior número: [maior_numero]
# Saida 2:  Menor número:: [menor_numero]

# numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# maior = max(numeros)
# menor = min(numeros)

# print(f'Maior número: {maior}')
# print(f'Menor número: {menor}')
 
#######################################################################
 
# Exercício: Contar Elementos
# Crie uma lista chamada animais com os seguintes elementos: "gato", "cachorro", "pássaro", "gato", "peixe".
# Conte quantas vezes o "gato" aparece na lista e exiba o resultado.
# Saida: O 'gato' aparece [contagem_gato] vezes na lista.
 
# animais = ["gato", "cachorro", "pássaro", "gato", "peixe"]

# contagem_gato = animais.count('gato')
# print(contagem_gato)
# print(f"O 'gato' aparece {contagem_gato} vezes na lista.") 
#######################################################################
 
 
# Exercício: Remover Duplicatas
# Crie uma lista chamada itens com os seguintes elementos: ["maçã", "banana", "maçã", "laranja", "banana", "uva"].
# Crie uma nova lista que contenha apenas os itens únicos (sem duplicatas) e exiba essa lista.
# Saida: Itens únicos [itens]

itens = ["maçã", "banana", "maçã", "laranja", "banana", "uva"]
print(itens)

itens_unicos = list(set(itens))
print(set(itens))
print(itens_unicos)