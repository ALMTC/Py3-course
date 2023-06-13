# caminho_aquivo = 'C:\\Users\\INSTITUTO IDEAR\\Documents\\VS Code\\Py3 course\\arquivos\\'
# caminho_aquivo += 'aula186.txt'

caminho_aquivo = 'arquivos\\aula186.txt'
# arquivo = open(caminho_aquivo, 'w')
#
# arquivo.close

with open(caminho_aquivo, 'w', encoding='utf-8') as arquivo:
    # print('abriu e fechou')
    arquivo.write("Atenção\n")
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))

with open(caminho_aquivo, 'r',encoding='utf-8') as arquivo:
    print(arquivo.read())

with open(caminho_aquivo, 'r',encoding='utf-8') as arquivo:
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())