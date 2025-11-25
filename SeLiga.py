def calcular_idade():

    nascimento = int(input("Digite o ano que você nasceu: "))
    anoAtual = 2025
    idade = anoAtual - nascimento
    print(f"Você tem {idade} anos\n")

def calcular_preco_compra():

    total_itens = int(input("Número de itens que você comprou?"))
    total = 0
    for i in range(total_itens):
        preco_item = float(input(f"Digite o preço do que você comprou{i+1}: R$ "))
        total += preco_item
    print(f"O total da sua compra é: R$ {total:.2f}\n")

def menu():

    while True:
        print("Se liga - MINI PROGRAMA COM MENU")
        print("1 - Calcular idade")
        print("2 - Calcular preço da compra")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            calcular_idade()
        elif opcao == '2':
            calcular_preco_compra()
        elif opcao == '3':
            print("Até logo!")
            break
        else:
            print("ERRO! Tente denovo.\n")


menu()
