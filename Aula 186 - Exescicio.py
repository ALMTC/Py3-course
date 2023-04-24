caminho_aquivo = 'C:\\Users\\INSTITUTO IDEAR\\Documents\\VS Code\\Py3 course\\arquivos\\'
caminho_aquivo += 'aula186.txt'

# arquivo = open(caminho_aquivo, 'w')
#
# arquivo.close

with open(caminho_aquivo, 'w') as arquivo:
    print('abriu e fechou')