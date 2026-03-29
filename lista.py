lista = [10, 20, 30, 40, 50]

print(lista)
leitura = len(lista)
print(leitura)
print(lista[0])
lista[0] = 100
print(lista)

contar = lista.count(100)
print(contar)

lista.append(60)
print(lista)

lista.insert(0,39)
print(lista)

indice = lista.index(100)
print(indice)

esta = 90 in lista
print(esta)

lista.remove(100)
print(lista)

lista.pop()
print(lista)

del lista[0]
print (lista)

lista.extend([7, 8, 9])
print(lista)

lista += [11, 12, 13]
print(lista)


