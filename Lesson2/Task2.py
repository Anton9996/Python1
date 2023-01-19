# Напишите программу, которая принимает 
# на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
try:
    coordA = []
    for i in range(2):
        coordA.append(int(input("введите координату точки А: ")))
    coordB = []
    for i in range(2):
        coordB.append(int(input('введите координату точки В: ')))
    print(coordA, coordB)

    distan = math.sqrt((coordB[0]- coordA[0])**2 + (coordB[1]- coordA[1])**2)
    print(round(distan, 3))
except:
    print('Введите числа')