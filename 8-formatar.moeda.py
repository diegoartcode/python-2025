import locale

# Definir o local para o formato do brasil

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

salario = 9999.99
# formatando o número como moeda
salario_formatado = locale.currency(salario, grouping = True)
print(salario)
print(salario_formatado)