salario = 9999.99

print(salario)

salario_formatado = f'{salario:,.2f}'.replace('.','x').replace(',','.').replace('x',',')

print(f'R$ {salario_formatado}')