# 15-condicional-comparacao-not.py

tenho_sede = True
tenho_fome = False

if tenho_sede and tenho_fome:
    print('Fazer um sanduiche e tomar um suco')
elif tenho_sede and not(tenho_fome):
    print('Tomar um suco')
elif not(tenho_sede) and tenho_fome:
    print('Fazer um sanduiche')
else:
    print('Ficar de boas!')