age = input("¿Cuál es tu edad (no mientas)?: ")

print(age)
age  = int(age)

if (age < 0 ):
    print ("Esto es serio, ve a jugar a otro lado 🤪")
elif (age >= 18):
    print("El usuario es mayor de edad 👍")
else:
    print("El usuario es menor de edad 🍼")
