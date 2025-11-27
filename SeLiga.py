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
        
   