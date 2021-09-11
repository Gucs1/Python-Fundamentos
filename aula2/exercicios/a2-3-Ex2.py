# Exercicio aula2- 3 - Dicionário
# Crie um sistema de cadastro de produtor
# o sistema deve solicitar ao usuário que informe os seguintes dados
# - Nome
# - Descrição
# - Categoria 
# - Valor
# O sistema deve atender as seguintes regras :
# - Permitir cadastrar produtor com valor maiores que 0
# - O nome do produto deve ter mais de 3 letras
# - A categoria deve possuir mais de 5 caracteres
# - Todos os dadis devem estar armazenados em um dicionario

# Exemplo
# nome = 'cerveja skol'
# Len(nome)

dicionario = {'Cerveja':'Budweiser', 'Descrição':'Budweiser, é uma cerveja do tipo long americana,fundada em 1876.', 'valor':3,}

print(dicionario['Cerveja'])
print(dicionario['Descrição'])
print(dicionario['valor'])

dicionario['Cerveja'] = 'Skol'
dicionario['Descrição'] = 'Skol é uma marca de cerveja de propriedade da empresa dinamarquesa Carlsberg, com licença para ser fabricada no Brasil'
dicionario['valor'] = 2

print(dicionario['Cerveja'])
print(dicionario['Descrição'])
print(dicionario['valor'])

Produto = {}
Produto2 = {}

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



