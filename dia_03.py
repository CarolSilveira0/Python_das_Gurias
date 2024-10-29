lista = ['Ana', 'Clara', 'Gabi', 'Dai']

# # len()
# print(len(lista))

# # fatiamento - pegar posição
# print(lista[0])
# # print(lista[1:3])

# # mudar valores
# lista[0] = 'Carol'
# lista[0:2] = ['Clara', 'Laura']


# # insert(posição, valor)
# lista.insert(2, 'Carol')


# # append()
# lista.append('Maria')


# # remove(valor) 
# # lista.remove('Maria')

# # pop(indice) -> vazio remove o ultimo
# lista2 = []
# nome = lista.pop(5)

# # lista2.append(nome)
# # print(lista2)

# #clear() -> esvazia a lista
# lista2.clear()

# # .sort() -> crescente por default
# lista.sort(reverse=True)

# .reverse() -> inverte a lista
# lista.reverse()


# # .copy() ou list(lista) ou lista[:] -> para copiar pra nova lista
# # var = lista.copy()
# lista2 = lista.copy()
# # lista2 = list(lista)
# # lista2 = lista[:]
# lista2[0] = 'Laura'
# print(lista2)
# print(lista)

# concatenar listas com + ou lista1.extend(lista2)
lista2 = ['João', 'Pedro', 'André']

lista3 = lista + lista2
lista.extend(lista2)
print(lista)

#.index(valor) -> pra saber o indice de determinado valor
print(lista.index('Dai'))

lista[3] = 'Dai Silva'

print(lista)


lista_teste = ['Ana', 'Osvaldo', 'ana', 'osvaldo']
lista.sort()