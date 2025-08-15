# 28-menu.py

def menu_principal():
    print('Menu principal')
    print('Digite o código do menu: ')
    print('1: Opção 1')
    print('2: Opção 2')
    print('3: Opção 3')
    print('4: Finalizar')
    print('5: Sair')

def submenu(opcao):
    print('########################')
    print(f'Você está na {opcao}')
    print('1: Fazer algo nessa sub opção')
    print('2: Voltar ao menu anterio')
    print('3: Sair')
    print('########################')

def main():  
    while True:
        menu_principal()

        opcao = input('Escolha uma opção: ')
        # print(opcao)

        if opcao == '1':
            # print('Opção 1 selecionada')
            submenu('Opção 1')
            sub_menu = input('Escolha uma ação')
            if sub_menu == '1':
                print('Você fez algo na opção 1')
            elif sub_menu == '2':
                continue
            elif sub_menu == '3':
                exit()
            else: 
                print('Opção invalida!')

        elif opcao == '2':
            # print('Opção 2 selecionada')
            submenu('Opção 2')
        elif opcao == '3':
            # print('Opção 3 selecionada')
            submenu('Opção 3')
        elif opcao == '4':
            print('Finalizar!')
            break
        elif opcao == '5':  
            print('Sair!!!')         
            exit()
        else:
            print('Opção invalida!')

main()

print('teste')