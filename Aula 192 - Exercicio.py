# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json

def processa(res):
    match res:
        case "listar":
            listar(lista_de_tarefas)
        case "desfazer":
            desfazer(lista_de_tarefas, itens_removidos)
        case "refazer":
            refazer(lista_de_tarefas, itens_removidos)
        case _:
            adicionar(res, lista_de_tarefas)

def listar(lista):
    print('')
    print('Tarefas a fazer: ')
    # for elemento in lista:
    #     print(elemento)
    print(*lista, sep='\n')
    print('')

def desfazer(lista, removido):
    removido.append(lista.pop(-1))
    listar(lista)

def refazer(lista, removido):
    lista.append(removido.pop(-1))
    listar(removido)

def adicionar(res, lista):
    lista.append(res)

def lerTarefas(tarefas, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except:
        salvarTarefas(tarefas, caminho)
    return dados


def salvarTarefas(tarefas, caminnho):
    dados = tarefas
    with open(caminnho, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'arquivos\\aula192.json'
lista_de_tarefas = lerTarefas([], CAMINHO_ARQUIVO)
itens_removidos = []

while True:
    print("Comandos: listar, desfazer, refazer")
    res = input("Digite uma tarefa ou comando: ")
    processa(res)
    salvarTarefas(lista_de_tarefas, CAMINHO_ARQUIVO)