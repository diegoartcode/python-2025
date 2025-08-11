# 23-repeticao-for-while.py

lista_numeros = [2,4,6,8]
lista_numeros = []
while True:
    num = int(input('Digite um numero: '))
    lista_numeros.append(num)
    for numero in lista_numeros:
        print(f'Contando até {numero}')
        contador = 1
        while contador <= numero:
            print(contador)
            contador += 1