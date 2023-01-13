import re

while True:
    cpf_cru = input('Digite o CPF a ser validado: ')
    cpf_sem_sinais = []
    soma_cpf = 0
    resto_soma_cpf = 0
    digito_verificacao1 = None
    digito_verificacao2 = None

    cpf_sem_sinais = re.sub(r'[^0-9]','',cpf_cru)

    #Primeiro dígito
    for i in range(9):
        numero_atual = int(cpf_sem_sinais[i])
        soma_cpf += numero_atual * (10-i)

    soma_cpf *= 10

    resto_soma_cpf = soma_cpf % 11

    digito_verificacao1 = resto_soma_cpf if resto_soma_cpf <= 9 else 0

    if digito_verificacao1 == int(cpf_sem_sinais[9]):
        print('Primeiro digito confere')
    else:
        print('Primeiro digito não confere')


    #Segundo dígito
    soma_cpf2 = 0

    for i in range(10):
        numero_atual = int(cpf_sem_sinais[i])
        soma_cpf2 += numero_atual * (11-i)

    soma_cpf2 *= 10

    resto_soma_cpf = soma_cpf2 % 11

    digito_verificacao2 = resto_soma_cpf if resto_soma_cpf <= 9 else 0

    if digito_verificacao2 == int(cpf_sem_sinais[10]):
        print('Segundo digito confere')
    else:
        print('Segundo digito não confere')