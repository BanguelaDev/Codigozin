import os

shoppingList = []
buying = True

while True:
    os.system('cls')

    print("Lista de compras atual:")
    for x in range(0, len(shoppingList)):
        print(x + 1, "-", shoppingList[x])

    if (buying == False):
        print("\nObrigado pela compra! Volte sempre.")
        break

    answer = input("\n\nBem vindo ao supermercado 4.5 estrelas!, o que deseja? \n 1 - Adicionar produto \n 2 - Remover produto \n 3 - Finalizar \n\n")

    match(answer):
        case "1":
            item = input("Digite o produto que você deseja adicionar \n")
            list.append(shoppingList, item)
        case "2":
            item = input("Digite o produto que você deseja remover \n")
            list.remove(shoppingList, item)
        case "3":
            buying = False
        case _:
            print("Não entendi, poderia repetir? \n")    
