import json


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

CAMINHO_ARQUIVO = 'arquivos\\aula206_classe_para_jason.json'

p1 = Pessoa('Lucas',27)
p2 = Pessoa('João',25)
p3 = Pessoa('Pedro',21)
dados = [vars(p1),vars(p2),vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, indent=2, ensure_ascii=False)
        print('Dados salvos')


if __name__ == '__main__':
    print('esse é o main')
    fazer_dump()
    
# def carregarPessoa(caminho):
#     dados = []
#     try:
#         with open(caminho, 'r', encoding='utf8') as arquivo:
#             dados = json.load(arquivo)
#         print('Dados carregados do arquivo')
#     except:
#         print('Sem dados salvos')
#     return dados

# def salvarPessoa(dados, caminnho):
#     dado = dados
#     with open(caminnho, 'w', encoding='utf8') as arquivo:
#         dado = json.dump(dados, arquivo, indent=2, ensure_ascii=False)
#     return dado

# CAMINHO_ARQUIVO = 'arquivos\\aula206_classe_para_jason.json'


# try:
#     p1 = Pessoa(carregarPessoa(CAMINHO_ARQUIVO)) # type: ignore
#     print('Carregou do arquivo')
# except:
#     p1 = Pessoa('Lucas', 27)
#     salvarPessoa(p1.__dict__, CAMINHO_ARQUIVO)

# #p1 = Pessoa('Lucas', 27)
# print(f'{p1.nome} tem {p1.idade} anos')
