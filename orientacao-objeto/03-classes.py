#Escoo da classe e de métodos da classe

class Animal:
    def __init__(self, nome):
        self.nome = nome

        soma = 2 + 2
        print(soma)
    def comendo(self, alimento):
        if(alimento[-1] == 'o'):
             return f'O {self.nome} está comendo o {alimento}'
        elif alimento[-1] == 'a':
            return  f'O {self.nome} está comendo a {alimento}'
        else:
            return f'O {self.nome} está comendo {alimento}'
        
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.comendo('macac'))