while True:
    numero_1 = input("Digite um número:")
    numero_2 = input("Digite outro número:")
    operador = input("Digite a operação (+ - / *):")
    
    resultado = ''
    
    try:
         numero_1_tratado = int(numero_1)
         numero_2_tratado = int(numero_2)
        
         if len(operador) > 1:
             print("Digite apenas um operador!!!")
             continue
         else:
            if(operador == '+'):
                resultado = numero_1_tratado + numero_2_tratado
            elif(operador == '-'):
                    resultado = numero_1_tratado - numero_2_tratado
            elif(operador == '/'):
                    resultado = numero_1_tratado / numero_2_tratado
            elif(operador == '*'):
                esultado = numero_1_tratado * numero_2_tratado
            else:
                print('Operador inválido, tente novamente')
                continue
    except:
        print("Valor digitado não é um número, tente novamente")
        continue
        
    print(resultado)
    
    encerrar = input("Deseja sair? s[im] n[ao]:").lower().startswith('s')
    
    if encerrar:
        print('Obrigado por usuário nosso serviço')
        break
    
    