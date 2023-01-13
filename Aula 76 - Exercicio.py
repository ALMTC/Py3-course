import os

palavra_secrta = 'teste'
numero_tentativas = 0
palavra_descobrir = ''

for i in palavra_secrta:
    palavra_descobrir += '*'

while '*' in palavra_descobrir:
    print(f'Palavra a ser descoberta: {palavra_descobrir}')

    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) != 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secrta:
        aux = ''
        for i in range(len(palavra_secrta)):
            letra_atual = palavra_secrta[i]
            if letra_digitada == letra_atual or palavra_descobrir[i] != '*':
                aux += letra_atual
            else:
                aux += '*'
        palavra_descobrir = aux
    else:
        print('Lentra não existe na palavra')

    numero_tentativas += 1

os.system('cls')
print(f'A palavra é {palavra_descobrir}!!!')
print(f'Você descobriu em {numero_tentativas} tentativas')
