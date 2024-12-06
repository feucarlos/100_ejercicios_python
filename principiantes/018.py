# https://docs.python.org/es/3/howto/sorting.html

l = [("Manzana", 15), 
                ("Banana", 8), 
                ("Fresa", 12), 
                ("Kiwi", 9), 
                ("Melocotón", 2)]

print(l)

l = sorted(l, key=lambda item:item[1]) 

print(l)