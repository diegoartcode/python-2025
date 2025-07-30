# 5-operadores-logicos.py

# operador logico E (and)
nome = True
senha = True

# resultado = nome == True and senha == True
resultado = nome and senha
print(resultado)
nome = 'Diegoss'
senha = '1234'

resultado = nome == 'Diego' and senha == '1234'

print(resultado)

# operador logico OU (or)

nome = 'Diego'
senha = '1234'
sobrenome = 'Rodrigues'

resultado = sobrenome == 'Rodrigues' or nome == 'Diego' or senha == '1234'

print(resultado)

# operador NÃO (not) 

variavel = False
resultado = variavel
print(not(resultado))