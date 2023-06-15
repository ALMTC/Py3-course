"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input('Digite um número inteiro: ')
# numero_inteiro = None

# try:
#     numero_inteiro = float(numero)
#     if numero_inteiro % 2 == 0:
#         print('Seu número é par')
#     else:
#         print('Seu número é impar')
# except:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Digite a hora atual: ')
# hora_inteiro = None

# try:
#     hora_inteiro = int(hora)
#     if 0 <= hora_inteiro <= 11:
#         print('Bom dia!')
#     elif 12 <= hora_inteiro <= 17:
#         print('Boa tarde!')
#     elif 18 <= hora_inteiro <= 23:
#         print('Boa noite!')
#     else:
#         print('Hora inválida')
# except:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if not nome.isdigit():
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Você não digitou um nome válido')