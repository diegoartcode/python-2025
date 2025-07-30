# 6-metodos.py

# nome_completo = input("Digite seu nome completo: ")
nome_completo = 'Diego Rodrigues21212'
print(f'1- Quantidade de caracteres: {len(nome_completo)}')

print(f'2 - Nome em maiúsculo: {nome_completo.upper()}')

print(f'3 - Nome em minúsculo: {nome_completo.lower()}')

print(f'4 - Nome sem espaço: {nome_completo.replace(' ','')}')

print(f'5 - Tem somente letras? (temos que tirar os espaços) {nome_completo.replace(' ', '').isalpha()}')

print(f'6 - É alfanumérico? Tem letras ou números (temos que tirar os espaços) {nome_completo.replace(' ', '').isalnum()}')

print(f'7 - Quebra o texto a cada espaço em branco: {nome_completo.split()}')
print(f'7 - Quebra o texto a cada espaço em branco: {nome_completo.upper().split()}')

print(f'8 - Centralizar o nome em *')
print('*******************Titulo*******************')
print(nome_completo.center(70,'*'))