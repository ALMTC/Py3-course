import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print('Produtos:')
print(*produtos , sep='\n')
print()

# Aumenta 10%
for produto in produtos:
    preco = produto.get('preco')
    preco = preco*1.1
    preco = float("{:.2f}".format(preco))
    produto.update({'preco': preco})

print('Produtos +10%:')
print(*produtos , sep='\n')
print()

#deepcopy
novos_produtos = copy.deepcopy(produtos)
print('Novos produtos deepcopy:')
print(*novos_produtos , sep='\n')
print()

#ordena por nome decrescente
order_by_name_decresent = sorted(produtos, key=lambda d: d['nome'], reverse=True)
print('Produtos ordenados por nome decrescente:')
print(*order_by_name_decresent , sep='\n')
print()

#depycopy e orderna por nome crescente
produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda d: d['nome'])
print('Produtos ordenados por nome crescente deepcopy:')
print(*produtos_ordenados_por_nome , sep='\n')
print()

#ordena por preço crescente
produtos_ordenados_por_preco = sorted(produtos, key=lambda d: d['preco'])
print('Produtos ordenados por preço:')
print(*produtos_ordenados_por_preco , sep='\n')
print()

#deepcoy produtos_ordenados_por_preco
produtos_ordenados_por_preco_copy = copy.deepcopy(produtos_ordenados_por_preco)
print('Produtos ordenados por preço deepcopy:')
print(*produtos_ordenados_por_preco_copy , sep='\n')
print()