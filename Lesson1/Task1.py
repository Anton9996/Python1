#1. Напишите программу, которая принимает 
# на вход два числа и проверяет, является ли 
# одно число квадратом другого.
#*Примеры:*
#- 5, 25 -> да
#- 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет

num1 = int(input('Первое число - '))
num2 = int(input('Второе число - '))

if num1 == num2*num2 or num2 == num1*num1:
    print(f'{num1},{num2} -> да')
else:
    print(f'{num1},{num2} -> нет')