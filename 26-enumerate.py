# 26-enumerate.py

frutas = ['maçã', 'uva', 'laranja', 'banana']
# for indice, fruta in enumerate(frutas, start=1):
#     print(indice, fruta)
    # print(fruta)
lista_frutas_list = list(enumerate(frutas))
print(lista_frutas_list)
lista_frutas_trupla = tuple(enumerate(frutas))
print(lista_frutas_trupla)
lista_frutas_set = set(enumerate(frutas))
print(lista_frutas_set)
lista_frutas_dict = dict(enumerate(frutas))
print(lista_frutas_dict)