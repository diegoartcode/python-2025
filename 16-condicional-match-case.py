from datetime import datetime

# opcao = 50

# match opcao:
#     case 1:
#         print('Opção 1 selecionada')
#     case 2:
#         print('Opção 2 selecionada')
#     case 3:
#         print('Opção 3 selecionada')
#     case _:
#         print('Opção invalida')

# dia = 'segunda'

# match dia:
#     case 'domingo':
#         print('Hojé é domingo')
#     case 'segunda':
#         print('Hojé é segunda')
#     case 'terça':
#         print('Hojé é terça')
#     case 'quarta':
#         print('Hojé é quarta')
#     case 'quinta':
#         print('Hojé é quinta')
#     case 'sexta':
#         print('Hojé é sexta')
#     case 'sabado':
#         print('Hojé é sabado')
#     case _:
#         print('valor invalido')
##################################



pegarDiaAtual = datetime.now()
print(pegarDiaAtual)
print(f'Data atual {pegarDiaAtual.strftime("%d/%m/%Y")}')
print(f"Data atual {pegarDiaAtual.strftime('%d/%m/%y')}")
print(f'Dia da semana {pegarDiaAtual.strftime('%A')}')
print(f'Dia da semana (abreviado) {pegarDiaAtual.strftime('%a')}')
print(f'Número do dia da semana {pegarDiaAtual.strftime("%w")}')
print(f'Número do dia do ano {pegarDiaAtual.strftime("%j")}')
print(f'Dia {pegarDiaAtual.strftime("%d")}')
print(f'Mês {pegarDiaAtual.strftime("%m")}')
print(f'Ano abreviado {pegarDiaAtual.strftime("%y")}')
print(f'Ano {pegarDiaAtual.strftime("%Y")}')


dia = pegarDiaAtual.strftime('%A').lower()
print(dia)
match dia:
    case 'sunday':
        print('Hojé é domingo')
    case 'monday':
        print('Hojé é segunda')
    case 'tuesday':
        print('Hojé é terça')
    case 'wednesday':
        print('Hojé é quarta')
    case 'thursday':
        print('Hojé é quinta')
    case 'friday':
        print('Hojé é sexta')
    case 'saturday':
        print('Hojé é sabado')
    case _:
        print('valor invalido')



################################################
import locale
locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')


dia = pegarDiaAtual.strftime('%A').lower()
print(dia)
match dia:
    case 'domingo':
        print('Hojé é domingo')
    case 'segunda-feira':
        print('Hojé é segunda')
    case 'terça-feira':
        print('Hojé é terça')
    case 'quarta-feira':
        print('Hojé é quarta')
    case 'quinta-feira':
        print('Hojé é quinta')
    case 'sexta-feira':
        print('Hojé é sexta')
    case 'sabado':
        print('Hojé é sabado')
    case _:
        print('valor invalido')


##############################################
pegarDiaAtual = datetime(2025, 8, 9, 14, 5, 20)
print(pegarDiaAtual)
dia = pegarDiaAtual.strftime('%A').lower()
print(dia)
match dia:
    case 'domingo':
        print('Hojé é domingo')
    case 'segunda-feira':
        print('Hojé é segunda')
    case 'terça-feira':
        print('Hojé é terça')
    case 'quarta-feira':
        print('Hojé é quarta')
    case 'quinta-feira':
        print('Hojé é quinta')
    case 'sexta-feira':
        print('Hojé é sexta')
    case 'sábado':
        print('Hojé é sabado')
    case _:
        print('valor invalido')