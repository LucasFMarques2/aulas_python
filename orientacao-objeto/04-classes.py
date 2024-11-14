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
        
    def stop(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto filma')
            return
        print(f'{self.nome} foto tirada')

c1 = Camera('Cannon')
c2 = Camera('tequepize')

c1.filmar()
c1.stop()
c1.fotografar()
c1.stop()


        