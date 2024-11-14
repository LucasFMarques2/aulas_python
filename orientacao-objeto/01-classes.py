class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Luiz', 'Freitas')
p2 = Pessoa('Maria', 'Rodriguies')

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)