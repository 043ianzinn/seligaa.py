import datetime 
def calcular_idade():
    ano_atual = datetime.datetime.now().year  # Obtém o ano atual
    
    while True:
        try:
            ano_nascimento = int(input("Digite o ano do seu nascimento (ex.: 1990): "))
            if ano_nascimento < 0:
                print("Erro: O ano de nascimento não pode ser negativo. Tente novamente.")
                continue
            if ano_nascimento > ano_atual:
                print(f"Erro: O ano de nascimento não pode ser maior que {ano_atual}. Tente novamente.")
                continue
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido para o ano de nascimento.")
    
    idade = ano_atual - ano_nascimento
    print(f"Sua idade aproximada é: {idade} anos.\n")

def calcular_preco_compra():
   
    while True:
        try:
            total_itens = int(input("Número de itens que você comprou? "))
            if total_itens < 0:
                print("Erro: O número de itens não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido para o número de itens.")
    
    total = 0.0
    for i in range(total_itens):
        
        while True:
            try:
                preco_item = float(input(f"Digite o preço do item {i+1}: R$ "))
                if preco_item < 0:
                    print("Erro: O preço não pode ser negativo. Tente novamente.")
                    continue
                total += preco_item
                break
            except ValueError:
                print("Erro: Digite um número válido para o preço (ex.: 10.50).")
    
    print(f"O total da sua compra é: R$ {total:.2f}\n")

def menu():
    while True:
        print("Se liga - MINI PROGRAMA COM MENU")
        print("1 - Calcular idade")
        print("2 - Calcular preço da compra")
        print("3 - Sair")
        
        
        opcao = input("Escolha uma opção (1-3): ").strip()  # Remove espaços extras
        
        if not opcao.isdigit() or len(opcao) != 1:
            print("Erro: Digite apenas um número de 1 a 3. Tente novamente.\n")
            continue
        
        opcao = int(opcao)  

        if opcao == 1:
            calcular_idade()
        elif opcao == 2:
            calcular_preco_compra()
        elif opcao == 3:
            print("Até logo!")
            break
        else:
            print("Erro: Opção inválida. Escolha 1, 2 ou 3.\n")


menu()
