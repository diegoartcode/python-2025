# 11-condicional-if-elif-else.py

# entrada nota 0 a 100

# se a nota maior ou igual a 90 # Saida Nota A
# se a nota maior ou igual a 80 # Saida Nota B
# se a nota maior ou igual a 70 # Saida Nota C
# se a nota menor 70 # Saida Nota D

nota = float(input('Digite sua nota: '))

if nota >= 90:
    print('Nota A')
elif nota >= 80:
    print('Nota B')
elif nota >= 70:
    print('Nota C')
else:
    print('Nota D ')