var_tplNome = ('Ana', True, '17/04/1986', 5000, 3800.50)
# print(var_tplNome[0])

var_listNome = list(var_tplNome)
var_listNome[0] = 'Clara'

var_tplNome = tuple(var_listNome)

# print(type(var_tplNome))
# print(var_tplNome)

# UNPACKING de TUPLA
nome, eh_funcionaria, data_nascimento, salario_bruto, salario_liquido = var_tplNome
print(nome)
print(eh_funcionaria)
print(data_nascimento)
print(salario_bruto)
print(salario_liquido)

var_listaDias = ['01/10/2024', '02/10/2024', '03/10/2024', '04/10/2024', '05/10/2024']

for indice, data in enumerate(var_listaDias):
    print(f'{indice} = {data}')