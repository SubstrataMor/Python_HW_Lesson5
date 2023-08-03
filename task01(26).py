# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree(a: int, b: int, multi = 1) -> int:
    if b == 0:
        return multi
    multi *= a
    return degree(a, b-1, multi)
    
a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(degree(a, b))