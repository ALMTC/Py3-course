import os

lista_compra = []
opcoes_validas = ['i', 'a', 'l']

while True:
    
    print('Selecione uma opção')
    print('[i]nserir  [a]pagar  [l]istar')
    opcao = input()

    if opcao in opcoes_validas:
        if opcao == 'i':
            valor = input('Digite o produto a ser adicionado: ')
            lista_compra.append(valor)
            
            os.system('cls')

            print('Produto adicionado com sucesso')

        elif opcao == 'a':
            val = input('Digite o indice do produto a ser excluído: ')

            try:
                val = int(val)

            except:
                print('O valor não é válido')
                continue

            if val < len(lista_compra) and val >= 0:
                lista_compra.pop(val)

                os.system('cls')
                
                print('Valor removido com sucesso')

            else:
                print('Indice inválido')

        else:
            os.system('cls')

            if lista_compra:
                print('Lista de produtos: ')
                for indice, valor in enumerate(lista_compra):
                    print(f'{indice} {valor}')
                print('')
            
            else:
                print('Nada a exibir')
                print('')
            

    else:
        print('Opção inválida')