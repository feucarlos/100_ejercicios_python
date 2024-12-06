# se crea la lista vacia
l = []

#se le asignan los valores
for i in range(1,9):
    l.append(i*3)

# se crea una nueva lista con comprensión de lista y los valores de 
# l divididos entre 3 (el libro no especifica tipo de dato y se usa float)
l1 = [item/3 for item in l]
print(l1)