import os
 
# Função para limpar a tela (compatível com Windows, Mac e Linux)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
 
# ============================================
# SISTEMA DE PEDIDOS
# ============================================
 
# Carrega tabela de preços
limpar_tela()
print("Carregando tabela de preços...")
precos = {
    'sanduiches': {
        'Big Mac': 20.00,
        'Duplo Quarteirão': 25.00,
        'Big Tasty': 22.00
    },
    'bebidas': {
        'Coca-Cola': 5.00,
        'Fanta': 5.00,
        'Del Valle Laranja': 6.00
    },
    'batatas': {
        'Pequena': 7.00,
        'Média': 9.00,
        'Grande': 11.00
    }
}
print("Tabela carregada com sucesso!\n")
 
# ===============================
# Funções para mostrar escolhas
# ===============================
 
def pegar_nome_cliente(nome):
    limpar_tela()
    print(f"Registrando nome do cliente...")
    print(f"Vamos iniciar o pedido - Cliente: {nome}")
 
def pegar_sanduiche(tipo_sanduiche):
    print(f"Você escolheu o sanduíche: {tipo_sanduiche}")
 
def pegar_bebida(tipo_bebida):
    print(f"Você escolheu a bebida: {tipo_bebida}")
 
def pegar_batata(tipo_batata):
    print(f"Você escolheu a batata do tamanho: {tipo_batata}")
 
def montar_combo(nome, tipo_sanduiche, tipo_bebida, tamanho_batata):
    limpar_tela()
    print("Montando combo completo...")
    pegar_nome_cliente(nome)
    pegar_sanduiche(tipo_sanduiche)
    pegar_bebida(tipo_bebida)
    pegar_batata(tamanho_batata)
 
# ===============================
# Funções de escolha de itens
# ===============================
 
def escolher_opcao_sanduiche():
    while True:
        limpar_tela()
        print("🔹 Escolha seu sanduíche:")
        sanduiche = input(
            '1 - Big Mac (R$ 20,00)\n'
            '2 - Duplo Quarteirão (R$ 25,00)\n'
            '3 - Big Tasty (R$ 22,00)\n'
            'V - Voltar\nS - Sair\n➡ '
        )
 
        if sanduiche.upper() == "V":
            return "voltar"
        elif sanduiche.upper() == "S":
            exit()
 
        opcoes = {'1': 'Big Mac', '2': 'Duplo Quarteirão', '3': 'Big Tasty'}
 
        if sanduiche in opcoes:
            return opcoes[sanduiche]
 
        print("Opção inválida, tente novamente.")
        input("Pressione ENTER para tentar de novo...")
 
def escolher_opcao_bebida():
    while True:
        limpar_tela()
        print("Escolha sua bebida:")
        bebida = input(
            '1 - Coca-Cola (R$ 5,00)\n'
            '2 - Fanta (R$ 5,00)\n'
            '3 - Del Valle Laranja (R$ 6,00)\n'
            'V - Voltar\nS - Sair\n➡ '
        )
 
        if bebida.upper() == "V":
            return 'voltar'
        elif bebida.upper() == "S":
            exit()
 
        bebidas = {'1': 'Coca-Cola', '2': 'Fanta', '3': 'Del Valle Laranja'}
 
        if bebida in bebidas:
            return bebidas[bebida]
 
        print("Opção inválida, tente novamente.")
        input("Pressione ENTER para tentar de novo...")
 
def escolher_opcao_batata():
    while True:
        limpar_tela()
        print("🔹 Escolha sua batata:")
        batata = input(
            '1 - Pequena (R$ 7,00)\n'
            '2 - Média (R$ 9,00)\n'
            '3 - Grande (R$ 11,00)\n'
            'V - Voltar\nS - Sair\n➡ '
        )
 
        if batata.upper() == "V":
            return 'voltar'
        elif batata.upper() == "S":
            exit()
 
        batatas = {'1': 'Pequena', '2': 'Média', '3': 'Grande'}
 
        if batata in batatas:
            return batatas[batata]
 
        print("Opção inválida, tente novamente.")
        input("Pressione ENTER para tentar de novo...")
 
# ===============================
# Sistema principal
# ===============================
pedidos_todos = []
 
while True:
    limpar_tela()
    nome_cliente = input("Digite o nome do cliente (ou [S] para sair): ")
 
    if nome_cliente.upper() == 'S':
        exit()
 
    pegar_nome_cliente(nome_cliente)
 
    while True:
        print("\nMENU PRINCIPAL")
        pedido = input(
            '1 - Somente sanduíche\n'
            '2 - Somente bebida\n'
            '3 - Somente batata\n'
            '4 - Combo\n'
            'F - Fechar caixa\n'
            'V - Voltar\n'
            'S - Sair\n➡ '
        )
 
        if pedido.upper() == "S":
            exit()
        elif pedido.upper() == "V":
            break
 
        pedido_cliente = {"sanduiche": None, "bebida": None, "batata": None}
 
        if pedido == '1':
            tipo_sanduiche = escolher_opcao_sanduiche()
            if tipo_sanduiche == 'voltar':
                continue
            limpar_tela()
            pegar_sanduiche(tipo_sanduiche)
            pedido_cliente['sanduiche'] = tipo_sanduiche
            input("\nPressione ENTER para continuar...")
 
        elif pedido == '2':
            tipo_bebida = escolher_opcao_bebida()
            if tipo_bebida == 'voltar':
                continue
            limpar_tela()
            pegar_bebida(tipo_bebida)
            pedido_cliente['bebida'] = tipo_bebida
            input("\nPressione ENTER para continuar...")
 
        elif pedido == '3':
            tipo_batata = escolher_opcao_batata()
            if tipo_batata == 'voltar':
                continue
            limpar_tela()
            pegar_batata(tipo_batata)
            pedido_cliente['batata'] = tipo_batata
            input("\nPressione ENTER para continuar...")
 
        elif pedido == '4':
            tipo_sanduiche = escolher_opcao_sanduiche()
            if tipo_sanduiche == 'voltar':
                continue
            tipo_bebida = escolher_opcao_bebida()
            if tipo_bebida == 'voltar':
                continue
            tipo_batata = escolher_opcao_batata()
            if tipo_batata == 'voltar':
                continue
            montar_combo(nome_cliente, tipo_sanduiche, tipo_bebida, tipo_batata)
            pedido_cliente['sanduiche'] = tipo_sanduiche
            pedido_cliente['bebida'] = tipo_bebida
            pedido_cliente['batata'] = tipo_batata
            input("\nPressione ENTER para continuar...")
 
        elif pedido.upper() == 'F':
            limpar_tela()
            print("Fechando o caixa...")
            print(f"Cliente: {nome_cliente}")
            total = 0
 
            for index, pedido in enumerate(pedidos_todos, 1):
                print(f"\nPedido {index}")
                if pedido['sanduiche']:
                    print(f"{pedido['sanduiche']} - R$ {precos['sanduiches'][pedido['sanduiche']]:.2f}")
                    total += precos['sanduiches'][pedido['sanduiche']]
                if pedido['bebida']:
                    print(f"{pedido['bebida']} - R$ {precos['bebidas'][pedido['bebida']]:.2f}")
                    total += precos['bebidas'][pedido['bebida']]
                if pedido['batata']:
                    print(f"{pedido['batata']} - R$ {precos['batatas'][pedido['batata']]:.2f}")
                    total += precos['batatas'][pedido['batata']]
 
            print(f"\nTotal do pedido: R$ {total:.2f}")
            pedidos_todos = []
            print("\nCaixa fechado com sucesso!")
            input("\nPressione ENTER para voltar ao menu...")
        else:
            print("Opção inválida, tente novamente.")
            input("\nPressione ENTER para continuar...")
 
        pedidos_todos.append(pedido_cliente)