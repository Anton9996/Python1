#2. Напишите программу, которая на вход принимает
# 5 чисел и находит максимальное из них.
# Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

def create_list():
    array = []
    for i in range(1,6):
        value = int(input("Введите число: "))
        array.append(value)
    return array
def find_max(array):
    max = array[0]
    for i in range(len(array)):
        if array[i]>max:
            max = array[i]
    return max
res = create_list()
print(res)
max = find_max(res)
print(f'максимальное значение {max}')