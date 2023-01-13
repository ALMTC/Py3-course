continuar = True

numeros_mult = []

while continuar:
    numero = input('Digite o número a ser multiplicado: ')
    if numero.isnumeric():
        numeros_mult.append(int(numero))
    else:
        continuar = False

def mult(args):
    contador = 1

    for numero in args:
        contador *= numero
    
    return contador

multiplicar = mult(numeros_mult)
print(multiplicar)
