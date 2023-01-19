# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

for x in range(4,6,1):
        for y in range(4,6,1):
            for z in range(4,6,1):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)