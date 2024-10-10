def multiplicador(*args):
    total = 1
    
    for numero in args:
        total *= numero
    return total


numeros_multiplicados = multiplicador(1,2,34,5,6,7)

print(1*2*34*5*6*7)
print(numeros_multiplicados)

def impar_ou_par(numero):
    if numero % 2 == 0:
        return 'par'
    return 'impar'

verifica_se_eh_impar_ou_par = int(input("Informe um número: "))


print(impar_ou_par(verifica_se_eh_impar_ou_par))