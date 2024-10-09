lista_de_compras = []
import os

while True:
    print("Bem-vindo(a) a nossa loja!")
    
    print("Informe o que deseja fazer")
    print("1-Adicionar item \n2-apagar item \n3-imprimir a lista")
    
    menu = input("Informe a opção:")
    
    try:
        menu = int(menu)
        
        if(menu == 1):
            os.system('clear')
            item = input("Informe o item que deseja adicionar:")
            lista_de_compras.append(item)

        elif(menu == 2):
            os.system('clear')
            item = input("Informe o item que deseja remover:")
            for itens in lista_de_compras[:]:
                if(item == itens):
                    lista_de_compras.remove(itens)
                else:
                    print("Item não exite")
                    continue
        elif(menu == 3):
            os.system('clear')
            if(len(lista_de_compras) < 1):
                print("Ainda não existe itens na lista")
            else:
                for indice, item in enumerate(lista_de_compras):
                    print(f'{indice + 1}-{item}')
        else:
            print("Valor informado é inválido")
            continue
    except:
        print("Valor informado não é inválido")
    