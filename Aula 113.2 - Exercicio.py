def parimpar(num):
    return 'O número é par' if num%2==0 else 'O número é impar'

numero = int(input('Digite o numero inteiro a ser verificado: '))

print(parimpar(numero))