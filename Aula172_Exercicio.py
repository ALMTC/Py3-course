# def ziper(lista1, lista2):
#     menor_lista = min(len(l1), len(l2))
#     return [
#         lista1[i] + lista2[i] for i in range(menor_lista)
#     ]

# l1 = [54,7,5,8,9,1,4,56,78,49]
# l2 = [65,7,45,27,84,7]

# print(list(ziper(l1,l2)))

l1 = [54,7,5,8,9,1,4,56,78,49]
l2 = [65,7,45,27,84,7]

lista_soma = [x + y for x, y in zip(l1,l2)]

print(lista_soma)