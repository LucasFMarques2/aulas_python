# Exercício - sistema de perguntas e respostas
import os

acertos = 0
qtd_de_perguntas = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print(pergunta['Opções'])
    resposta = input("Informe a resposta: ")
    qtd_de_perguntas += 1
    
    if resposta == pergunta['Resposta']:
        os.system('clear')
        print("Parabéns você acertou!")
        acertos += 1
    else:
        print("Errou")
        
print(f"Você acertou {acertos} de {qtd_de_perguntas} perguntas")