# Напишите программу, которая принимает
#  на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def coordinates(numX,numY):
    if numX > 0 and numY > 0: 
        print(f'- {numX,numY} -> 1 ')
    elif numX < 0 and numY < 0: 
        print(f'- {numX,numY} -> 3 ')
    elif numX < 0 and numY > 0: 
        print(f'- {numX,numY} -> 2 ')
    elif numX > 0 and numY < 0: 
        print(f'- {numX,numY} -> 4 ')
    else:
        print(f'Укажите значения не равные 0 ')
try:
    numX = int(input('Введите значаение по оси x:  '))
    numY = int(input('Введите значаение по оси y:  '))
    coordinates (numX,numY)
except:
    print ('Укажите значения не равные 0')