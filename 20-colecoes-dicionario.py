meses = {
    1 : 'Janeiro',
    2 : 'Fevereiro',
    3 : 'Março',
    4 : 'Abril',
    5 : 'Maio',
    6 : 'Junho'
}

print(meses)
print(type(meses))
print(meses[1])

meses = {
    'jan' : 'Janeiro',
    'fev' : 'Fevereiro',
    'mar' : 'Março',
    'abr' : 'Abril',
    'mai' : 'Maio',
    'jun' : 'Junho'
}

print(meses['abr'])
meses['jun'] = "JUNHO" # modificando
print(meses)
meses['jul'] = 'Julho' # adicionando
print(meses)
meses.pop('jan') # excluir
print(meses)

# Dicionario aninhado

produtos = {
    'produto1':{
        'nome' : 'Maça',
        'preco': '6.50'
    },
    'produto2':{
        'nome' : 'Banana',
        'preco': '9.99'
    }
}
print(produtos['produto1']['nome'])
print(produtos['produto1']['preco'])
print(produtos['produto2']['nome'])
print(produtos['produto2']['preco'])

chaves = ['nome','idade','curso']
valores = ['Diego',33,'Python']
print(type(chaves))
print(type(valores))

pessoa = dict(zip(chaves,valores))

print(pessoa)
print(type(pessoa))

print(pessoa['nome'])