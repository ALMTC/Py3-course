import json
from Aula206a_Exercicio import Pessoa, CAMINHO_ARQUIVO,fazer_dump

fazer_dump()

lista_pessoas = []

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)

for dado in dados:
    lista_pessoas.append(Pessoa(**dado))

for pessoa in lista_pessoas:
    print(f'{pessoa.nome} tem {pessoa.idade} anos')