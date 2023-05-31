import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

caminho_arquivo = "arquivos\\aula 190.json"

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, indent=2)

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    pessoa2 = json.load(arquivo)
    print(pessoa2)