print("Impares de 10 a 20 con for")

for i in range(10,21):
    if (i % 2 == 1):
        print(i)


print("\nImpares de 10 a 20 con while")
j = 10
while (j <= 20):
    if (j % 2 == 1):
        print(j)
    j += 1
