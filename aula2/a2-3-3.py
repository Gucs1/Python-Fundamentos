# Curso: Python Fundamentos Proway
# Aula : Dia 2 - Parte 3
# Assunto: Dicionários
# Data: 2021-08-28

#bebidas = 

lista = ['listagem1']
tuplas = ('gustavo')

lista[0]
tuplas[0]

# criando um dicionario
dicionario = {'nome':'Gustavo', 'sobrenome':'Coelho', 'idade':10,}

# lendo um dicionario
print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])


# alternando dados de um dicionario
dicionario['nome'] = 'Tamires'
dicionario['sobrenome'] = 'Azeredo'
dicionario['idade'] = 17

# lendo dados alterados
print(dicionario['nome'])
print(dicionario['sobrenome'])
print(dicionario['idade'])

# adicionando um novo conjunto d chave:valor
dicionario['cpf'] = '5912390817'
print(dicionario['cpf'])

# 
cliente = {}
clientes2 = {'nome':'', 'sobrenome':'', 'idade':19}

cliente['nome']= input('Digite seu nome: ')
cliente['sobrenome']= input('Digite o sobrenome: ')
cliente['idade']= int(input('Digite a idade: '))

print(cliente)
# deletando uma chave dicionario de um dicionario
del(cliente['idade'])
print(cliente)
