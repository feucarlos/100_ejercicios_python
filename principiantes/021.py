dic = {"Manzana": 15,
       "Banana": 8,
       "Fresa": 12,
       "Kiwi": 9,
       "Melocotón": 2
       }

frutas = 0

for fruta in dic:
    frutas += dic[fruta]

print("Frutas: ", frutas)