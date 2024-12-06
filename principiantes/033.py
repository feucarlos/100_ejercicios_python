# https://docs.hektorprofe.net/python/funcionalidades-avanzadas/funcion-filter/

l = [-6, 5, -3, -1, 2, 8, -3.6]

l1 = [num for num in list(filter(lambda pos: pos>=0, l))]

print(l1)