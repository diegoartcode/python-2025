# Exercício 1: 
# Solicite ao usuário que insira seu nome e idade. Em seguida, exiba uma mensagem de boas-vindas. 
# mensagem Olá, [nome]! Você tem [idade] anos. 

# nome = input('Digite seu nome: ')
# idade = input('Digite sua idade: ')
# print(f'Olá, {nome}! Você tem {idade} anos. ')
  
################################################################# 
  
# Exercício 2: 
# Crie uma variável chamada nome_completo para armazenar o nome completo de uma pessoa. 
# Crie outra variável chamada idade para armazenar a idade da pessoa. 
# Crie uma variável salario_mensal para armazenar o salário mensal da pessoa. 
# Por fim, exiba essas informações de forma concatenada no seguinte formato: 
# "Meu nome é [nome_completo], tenho [idade] anos e ganho R$ [salario_mensal] por mês."
 
# nome_completo = input('Digite seu nome completo')
# idade = input('Digite sua idade')
# salario_mensal = input('Digite seu salario: ')
# print(f'Meu nome é {nome_completo}, tenho {idade} anos e ganho R$ {salario_mensal} por mês.')

##* Extra Formatar o salario_mensal como moeda 
# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# nome_completo = input('Digite seu nome completo')
# idade = input('Digite sua idade')
# salario_mensal = float(input('Digite seu salario: '))
# formatacao_salario = locale.currency(salario_mensal, grouping = True)
# print(f'Meu nome é {nome_completo}, tenho {idade} anos e ganho R$ {formatacao_salario} por mês.')
  
################################################################# 
  
# Exercício 3: 
# Solicite ao usuário dois números inteiros e exiba a soma dos números. 

# numero1 = int(input('Digite o primeiro número inteiro: '))
# numero2 = int(input('Digite o segundo número inteiro: '))

# soma = numero1 + numero2
# print(f'A soma dos números é: {soma}')
  
################################################################# 
  
#Exercício 4: 
# Peça ao usuário que insira um número decimal (float) e exiba o dobro desse número. 
# Saida = O dobro de ? é ?. 
# exemplo = entrada 5 então a saida seria "O dobro de 5 é 10" 

# numero_decimal = float(input('Digite um número decimal: '))
# dobro = numero_decimal * 2
# print(f'O dobro de {numero_decimal} é {dobro}')
  
################################################################# 
  
# Exercício 5: 
  
# Peça ao usuário que insira seu nome e se está estudando atualmente (responda com "sim" ou "não"). Exiba uma mensagem confirmando sua resposta. 
# entrada = Digite seu nome 
# entrada = Está estudando atualmente, digite "sim" ou "não  
## temos que tratar o valor de entrada "sim" ou "não com .strip().lower() 
# saida =[nome], você está estudando: [esta_estudando].") 
# a variavel [esta_estudando] vai ser igual a true ou false 
  
###### 

# nome = input('Digite seu nome: ')
# estudando = input('Está estudando atualmente, digite "sim" ou "não"')
# esta_estudando = (estudando.strip().lower() == 'sim')
# print(f'{nome}, você está estudando: {esta_estudando}.') 

# if esta_estudando == True:
#     print(f'{nome}, ótimo continue assim!')
# else:
#     print(f'{nome}, vamos estudar! ')

# if esta_estudando:
#     print(f'{nome}, ótimo continue assim!')
# else:
#     print(f'{nome}, vamos estudar! ')

## Extra implementar if else 
## se a variavel [esta_estudando] = True  
## saida = [nome], ótimo continue assim! 
## se não  
## saida = [nome], vamos estudar! 
  
################################################################# 
  
# Exercício 6: 
# Peça ao usuário para inserir seu nome e um número, depois exiba o nome repetido esse número de vezes. 

# nome = input("Digite seu nome: ")
# vezes = int(input('Digite um número: '))

# print((nome + '\n') * vezes)
  
################################################################# 
  
# Exercício 7: 
# Solicite ao usuário que insira seu peso e altura, calcule seu IMC (Índice de Massa Corporal) e exiba o resultado. 
# Fórmula do IMC: IMC = peso / altura² 

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))

# # imc = peso / (altura ** 2 )
# imc = peso / (altura * altura )
   
# print(f'Seu IMC é: {imc:.2f}')
 
################################################################# 
  
# Exercício 8: 
# Solicite ao usuário que insira a quantidade de horas trabalhadas e o valor da hora. Calcule e exiba o salário bruto. 

horas_trabalhada = float(input('Digite a quantidade de horas trabalhadas: '))
valor_hora = float(input('Digite o valor da hora (R$): '))

salario_bruto = horas_trabalhada * valor_hora

print(f'Seu salário bruto é: R$ {salario_bruto:.2f}')
################################################################# 
  
# Exercício 9: 
# Solicite ao usuário um valor de produto e uma porcentagem de desconto. Calcule e exiba o valor final com o desconto aplicado. 

valor_produto = float(input('Digite o valor do produto: '))
porcentagem_desconto = float(input('Digite a porcentagem de desconto (%)'))
desconto = valor_produto * (porcentagem_desconto / 100)
valor_final = valor_produto - desconto
print(f'O valor final com desconto é R${valor_final:.2f}')