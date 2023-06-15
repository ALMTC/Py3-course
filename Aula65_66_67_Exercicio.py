while True:
    
    try:
        numero_1 = float(input('Digite o primeiro número: '))
        numero_2 = float(input('Digite o segundo número: '))
    except:
        print('O valor digitado não é válido')
        continue

    operacao = input('Digite a operação: ')

    operadores_permitidos = '+-*/'

    if operacao in operadores_permitidos and len(operacao) > 1:

        match operacao:
            case '+':
                print(f'Resultado: {numero_1 + numero_2}')
            case '-':
                print(f'Resultado: {numero_1 - numero_2}')
            case '*':
                print(f'Resultado: {numero_1 * numero_2}')
            case '/':
                print(f'Resultado: {numero_1 / numero_2}')
    else:
        print('Sinal de operação inválido')
        continue

    sair = input('Deseja sair da aplicação? [s]im: ').lower().startswith('s')

    if sair:
        break