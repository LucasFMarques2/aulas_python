#Métodos de instãncias de classes Python
'''
Classe - Molde (geralmente sem dados)
Instância da class (objeto) - Tem os dados
Uma classe pode gerar várias instância.
'''
class Carro:
    def __init__(self, nome):
        self.nome = nome # Hard Coded
        
    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')
print(fusca.nome) 
fusca.acelerar()

        
