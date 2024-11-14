#Matendo o estado dentro da class

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return 
        print(f'{self.nome} está filmando')
        self.filmando = True
        


c1 = Camera('Cannon')
c2 = Camera('tequepize')

c1.filmar()
c1.filmar()

        