print('Carregando tabela de preços...')
precos = {
    'sanduiches': {
        'Big Mac' :20.00,
        'Duplo Quarteirão' : 25.00,
 
    },
    'bebidas' :{
        'Coca-Cola' : 5.00,
        'Fanta' : 5.00,
        'Del Valle Laranja' : 6.00
    },
    'batata' : {
        'Pequena' : 7.00,
        'Média' : 9.00,
        'Grande' : 11.00
    }
}
 
def pegar_nome_cliente(nome):
    print('Registrando o nome o cliente...')
    print(f'Vamos iniciar o pedido - Cliente: {nome}')
 
def escolha_opcao_sanduiche():
    while True:
        print('Esolha seu sanduiche')
        sanduiche = input(
            '1 - Big mac (R$ 20,00)\n'
            '2 - Duplo Quarteirão (R$ 25,00)\n'
            '3 - Bih tasty (R$ 22,00)\n'
            'V - Voltar\n'
            'S - Sair\n'
        )
        if sanduiche.upper() == "V":
            return 'voltar'
        elif sanduiche.upper() == "S":
            exit()
 
        opcoes = {'1': 'Big Mac', '2': 'Duplo Quarteirão', '3': 'Big Tasty'}
        if sanduiche in opcoes:
            return opcoes[sanduiche]
       
        print('Opção invalida, tente novamente. ')
        input('Pressione ENTER para tentar de novo...')
 
def pegar_sanduiche(tipo_sanduiche):
    print(f'Você escolheu o sanduiche: {tipo_sanduiche}')
 
pedidos_todos = []
 
while True:
    nome_cliente = input('Digite o nome do cliente ( ou [s] para sair.): ')
    if nome_cliente.upper() == 'S':
        exit()
    pegar_nome_cliente(nome_cliente)
    while True:
        print('\n MENU PRINCIPAL')
        pedido = input(
            '1 - Somente saduiche\n'
            '2 - Somente bebida\n'
            '3 - Somente batata\n'
            '4 - Combo\n'
            'F - Fechar caixa\n'
            'V - Voltar\n'
            'S - Sair\n'
        )
        if pedido.upper() == 'S':
            exit()
        elif pedido.upper() == 'V':
            break
 
        pedido_cliente = {
            'sanduiche': None,
            'bebida': None,
            'batata' : None
            }
       
        if pedido == '1' :
            print('Voce escolheu a opção 1')
            tipo_sanduiche = escolha_opcao_sanduiche()
            if tipo_sanduiche == 'voltar':
                continue
            pegar_sanduiche(tipo_sanduiche)
            pedido_cliente['sanduiche'] = tipo_sanduiche
            input('\nPressione ENTER para continuar')
        elif pedido == '2':
            print('Você escolheu a opção 2')
        elif pedido == '3':
            print('Voce escolheu a opção 3')
        elif pedido.upper() == 'F':
            print('Fechando o caixa.....')
            print(f'Cliente: {nome_cliente}')
            total = 0
 
            print(pedidos_todos)
            for index,pedido in enumerate(pedidos_todos, 1):
                print(f'\nPedido {index}')
                if pedido['sanduiche']:
                    print(f'{pedido['sanduiche']} - R$ {precos['sanduiches'][pedido['sanduiche']]:.2f}')
                    total += precos['sanduiches'][pedido['sanduiche']]
 
            print(f'\n Total do pedido: R$ {total: .2f}')
            print('\nPedido fechado com suacesso!')
            input('\nPressione ENTER para voltar ao menu...')
        pedidos_todos.append(pedido_cliente)