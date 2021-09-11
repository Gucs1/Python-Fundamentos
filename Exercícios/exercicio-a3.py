# Exercicio 1 - aulas funções procedimentos
# Crie um sistema de cadastro de produtos
# O sistema deve ter 4 funcoes
# 1 - imprimir um cabecalho
# utilizar a biblioteca para limpar tela
# 2 - Funcao que solicita os dados do produto
# usar as funcoes input para solicitar nome, descricao e valor
# salvar os dados em um dicionario
# retornar ao dicionarioao final da funcao
# 3 -  funcao de validacao de ados
# deve validar se o nome do produto maior que os 5 caracteres
# validar se o valor maoir que zero
# 4- imprimir um rodapé e os dados do produto cadastrado

import os 

dicionario = {'Cerveja':'Budweiser', 'Descrição':'Budweiser, é uma cerveja do tipo long americana,fundada em 1876.', 'valor':3,}
print(dicionario['Cerveja'])
print(dicionario['Descrição'])
print(dicionario['valor'])
os.system('cls' if os.name == 'nt'else 'clear')

dicionario['Cerveja'] = 'Skol'
dicionario['Descrição'] = 'Skol é uma marca de cerveja de propriedade da empresa dinamarquesa Carlsberg, com licença para ser fabricada no Brasil'
dicionario['valor'] = 2

print(dicionario['Cerveja'])
print(dicionario['Descrição'])
print(dicionario['valor'])

Produto = {}
Produto2 = {}

os.system('cls' if os.name == 'nt'else 'clear')
print('*'*15, 'Cadastro de Produtos', '*'*15)
print('\n')
Produto['produto']= input('Digite o produto: ')
Produto['descrição']= input('Digite a Descrição: ')
Produto['valor']= int(input('Digite o valor: '))
print(Produto)

Produto2['produto']= input('Digite o produto: ')
Produto2['descrição']= input('Digite a Descrição: ')
Produto2['valor']= int(input('Digite o valor: '))
print(Produto2)
Produtos = [Produto, Produto2]
print(Produtos)
print('Cadastrado com sucesso!')



