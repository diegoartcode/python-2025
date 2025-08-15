# 29-limpar-tela.py
import os


print('Teste')

def limpar_tela():
    # para sistema Unix (Linux e MacOS)
    if os.name == 'posix':
        os.system('clear')
    # para windows
    elif os.name == 'nt':
        os.system('cls')
    else:
        print('\n' * 120) #imprime linhas em branco para simular a limpeza
limpar_tela()
print('Este texto aparecerá após a limpeza.')
