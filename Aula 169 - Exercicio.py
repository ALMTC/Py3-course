from itertools import zip_longest

def ziper(lista1, lista2):
    menor_lista = min(len(l1), len(l2))
    return [
        (lista1[i],lista2[i]) for i in range(menor_lista)
    ]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(ziper(l1,l2))

print(list(zip(l1,l2)))

print(list(zip_longest(l1,l2)))

print(list(zip_longest(l1,l2, fillvalue="Sem cidade")))