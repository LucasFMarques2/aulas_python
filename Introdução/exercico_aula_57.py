numero = input("Informe um número:")


try:
   numero_formatado = int(numero)
   if(numero_formatado % 2 == 0):
      print("Esse número é par")
   else:
      print("Esse número é impar")
except:
    print("Número informado não é um número inteiro")


horario = input("Informe um horário formato 24h: ")

try:
    horario_formatado = int(horario)
    if(horario_formatado <= 11):
        print("Bom dia")
    elif(horario_formatado >= 12 and horario_formatado <= 17):
        print("Boa tarde")
    else:
        print("Boa noite")
except:
    print("Valor informado não é um número")


nome = input("Informe seu primeiro nome: ")

if(len(nome) <= 4):
    print("Seu nome é curto")
elif(len(nome) >= 5 and len(nome) <= 6):
    print("Sei nome é normal")
else:
    print("Seu nome é muito grande")