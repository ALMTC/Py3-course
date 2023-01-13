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

acertos = 0
total_perguntas = len(perguntas)

for pergunta in perguntas:
    print(f'Pergunta: {pergunta["Pergunta"]}')

    opcoes = pergunta['Opções']
    print('\nOpções')

    for indice, opcao in enumerate(opcoes):
        print(f'{indice}) {opcao}')
    
    print('')
    resposta = input('Digite o índice da resposta: ')
    resposta = int(resposta)

    if opcoes[resposta] == pergunta['Resposta']:
        print('Resposta correta!!!')
        acertos += 1
    else:
        print('Resposta errada')
    print('')

print(f'Você acertou {acertos} de {total_perguntas} respostas')