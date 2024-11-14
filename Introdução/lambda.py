lista = [
    {'nome': 'Lucas', 'sobrenome': 'Freitas'},
    {'nome': 'Caio', 'sobrenome': 'Saza'},
    {'nome': 'Ana', 'sobrenome': 'UmMuitoBom'},
    {'nome': 'Polly', 'sobrenome': 'Creme'},
    {'nome': 'Açucars', 'sobrenome': 'Doce'},
]

#funcao anonima lambda

def exibir(lista):
    for item in lista:
        print (item)
    print()
l1 = sorted(lista,key=lambda item: item['nome'])
l2 = sorted(lista,key=lambda item: item['sobrenome'])



exibir(l1)

#list comprehesion

lista_2 = [numero * 2 for numero in range(10)]

print(lista_2)

#mapeamento em list comprehesion

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 50},
    {'nome': 'p3', 'preco': 10},
]

novos_produtos =[
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos
]

print(*novos_produtos, sep='\n')

def multiplica(x ,y):
    return x * y

numeros = [1,2,3,4,5,6,7]
multiplica = [multiplica(numero, 2) for numero in numeros]

print(multiplica)

#condicional

numeros=[1,2,3,4,5,6,7,8,9,10]
transofromar_numero = [numero if numero != 6 else 600 for numero in numeros]

print(transofromar_numero)