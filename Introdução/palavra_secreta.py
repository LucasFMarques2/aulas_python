import os

palavra_secreta = 'carro'
letra_acertada = ''
tentativas_restantes = 6
numero_de_tentativas = 0
nome = input("Informe seu nome: ")

while True:
    if tentativas_restantes > 0:
        print(f"Olá {nome}, você tem {tentativas_restantes} para acertar a palavra")
        letra_digitada = input("Informe uma letra:")

        
        if len(letra_digitada) > 1:
            print("Digite apenas uma letra!!!")
            continue
        
        tentativas_restantes -= 1
        numero_de_tentativas += 1
        
        palavra_acertada = ''
        
        if letra_digitada in palavra_secreta:
            letra_acertada += letra_digitada
            
        for letra_secreta in palavra_secreta:
            if letra_secreta in letra_acertada:
                palavra_acertada += letra_secreta
            else:
                palavra_acertada += '*'
    
        print(f'a palavra é: {palavra_acertada}')
        print(f'Número de tentativas restantes: {tentativas_restantes}')
        
        if palavra_acertada == palavra_secreta:
            os.system("clear")
            print(f'Parabéns, você acertou em {tentativas_restantes}, a palavra era: {palavra_secreta}')
            jogar_novamente = input("Deseja jogar novamente? s[im] n[nao]").lower().startswith('s')
            
            if jogar_novamente:
                os.system("clear")
                letra_acertada = ''
                palavra_acertada = ''
                tentativas_restantes = 0
                numero_de_tentativas = 10
                continue
            else:
                print("Vlw por jogar")
                break
    else:
        print("Você já usou todas as tentativas!!!")
        break   