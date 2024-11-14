
##Calculo do primeiro dígito
import re


cpf = '706.103.621-43'
cpf = re.sub(r'[^0-9]', '',cpf)
nove_digitos = cpf[:9]

tratar_cpf = re.split(r'[. -]', nove_digitos)

tratar_cpf = ''.join(tratar_cpf)

numero_tratado = 0

resultado_primeiro_digito = 0
multiplicador = 10

for numero in tratar_cpf:
    numero_tratado = int(numero)
    resultado_primeiro_digito += numero_tratado * multiplicador
    multiplicador -= 1
    
resultado_primeiro_digito *= 10
resultado_primeiro_digito %= 11

resultado = resultado_primeiro_digito if resultado_primeiro_digito <= 9 else 0

##Calculo do segundo dígito
resultado_primeiro_digito = str(resultado_primeiro_digito)

tratar_cpf = list(tratar_cpf)
tratar_cpf.append(resultado_primeiro_digito)
tratar_cpf = ''.join(tratar_cpf)

multiplicador = 11
resultado_segundo_digito = 0

for numero in tratar_cpf:
    numero_tratado = int(numero)
    resultado_segundo_digito += numero_tratado * multiplicador
    multiplicador -= 1

resultado_segundo_digito *= 10
resultado_segundo_digito %= 11

resultado_segundo_digito = resultado_segundo_digito if resultado_segundo_digito <= 9 else 0

tratar_cpf = list(tratar_cpf)
tratar_cpf.pop()
tratar_cpf = ''.join(tratar_cpf)

validador_de_cpf = (f'{tratar_cpf}{resultado_primeiro_digito}{resultado_segundo_digito}')

cpf_para_validacao = re.sub(r'[^0-9]','',cpf)
cpf_para_validacao = ''.join(cpf_para_validacao)

if validador_de_cpf == cpf_para_validacao:
    print("CPF é válido")
else:
    print("CPF é inválido")




    
    
    
    

    

