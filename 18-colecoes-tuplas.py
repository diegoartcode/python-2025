# 18-colecoes-tuplas.py
# uma tupla (tuple) em python é uma sequência imutável de valores de qualquer tipo 

coordenadas = (-49,200,-20,80,200)
print(coordenadas)

print(type(coordenadas))

# coordenadas[2] = 10000000
# print(coordenadas)

print(coordenadas[2])

print(len(coordenadas)) # retorna a quantidade de itens detro da coleção

coordenadas2 = (50,-10,60,45)

coordenadas_concatenada = coordenadas + coordenadas2
print(coordenadas_concatenada)

pessoas = ['Diego','Jhenny','Fabio','Mauro']
print(pessoas)
print(type(pessoas))
pessoas_tupla = tuple(pessoas)
print(pessoas_tupla)
print(type(pessoas_tupla))

pessoa = ('Diego', 33, 'Desenvolvedor')

print(pessoa[0])

nome, idade, profissao = pessoa
print(nome)
print(idade)
print(profissao)

tupla_aninhada = (
    ('Maça',1),
    ('Banana',2),
    ('Laranja',3)
)

print(tupla_aninhada[2][0])