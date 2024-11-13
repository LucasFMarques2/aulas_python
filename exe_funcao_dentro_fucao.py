def cria_multiplicador(number):
    def multi_number(multiplicador):
        return number * multiplicador
    return multi_number

multiplicador = cria_multiplicador(int(input("Informe um número: ")))

numero_multiplicado = multiplicador(int(input("Informe outro número: ")))

print(numero_multiplicado)
