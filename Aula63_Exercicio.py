nome = 'Antonio Lucas'
tamanho_nome = len(nome)
contador = 0
nova_str = ''

while contador < tamanho_nome:
    nova_str += f'*{nome[contador]}'
    contador += 1

print(nova_str)