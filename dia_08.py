# declaração dicionário
var_dictVazio = {}

var_dictDicionario = {
    'nome': 'Carolina Reis',
    'idade': 38,
    'casada': True,
    'altura': 1.56,
    'pais': ['Jussara', 'Paulo']
    }

var_dictDicionario2 = {'nome': 'Carol', 'idade': 38}

var_dictTupla = dict(name='Carol', idade=39)

# modificar dicionário:
var_dictDicionario['nome'] = 'Carolina Reis Martins'

# acrescentar nova chave:
var_dictDicionario['irmaos'] = ['Lara', 'Kelen']

var_dictVazio['emissor'] = 'Fulano'
var_dictVazio['data'] = '26/11/2024'
var_dictVazio['valor'] = 1200.00

var_dictVazio.clear()
# print(var_dictVazio)
# print(var_dictDicionario)

var_listChaves = var_dictDicionario.keys()
var_listValores = var_dictDicionario.values()
# print(var_listValores)

for x, y in var_dictDicionario.items():
  print(x, y)
  
# UNPACKING TUPLA
tupla = ('Carol', 38, 1.56, True)

nome, idade, altura, casada = tupla

print(altura)

var_dictDicionario = {
    'Carol': {'nome': 'Carolina Reis','idade': 38},
    'Dai': {'nome': 'DAi','idade': 28},
    'Gabi': {'nome': 'GAbi', 'idade': 38}
    }

print(var_dictDicionario['Dai']['idade'])

