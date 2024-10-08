nome = 'Lucas Freitas'
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    indice += 1
    novo_nome += f'*{letra}'

novo_nome += '*'
print(novo_nome)