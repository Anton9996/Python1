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

#try:
#    numbers = []
#    for i in range(5):
#    numbers.append(int(input(f'Введите число {i+1}: ')))
#    max_num = numbers[0]
#    min_num = numbers[0]
#    index_max = 0
#    index_min = 0
#    sum = 0
#    for i in range(len(numbers)):
#        sum += numbers[i]
#        if numbers[i] > max_num:
#            max_num = numbers[i]
#            index_max = i
#        elif numbers[i] < min_num:
#            min_num = numbers[i]
#            index_min = i
#    print('Максимальное число =', max_num, 'Индекс = ', index_max)
#    print('Минимальное число =', min_num, 'Индекс = ', index_min)
#    print('Среднее арифметическое = ', sum/len(numbers))
#except:
#    print('Введите целое число')