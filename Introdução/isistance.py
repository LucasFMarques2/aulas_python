lista = [
    'a', 1, 1.1,True,[0,1,2], (1,2),
    {0,1},{'nome': 'lucas'}
]

for item in lista:
    if isinstance(item, dict):
        print('Discionary: ', item)