# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random
n = int(input("Введите число N: "))
list = []
for i in range(0,n):
    list.append(int(random.randint(n*-1, n)))
print(list)

choice=input(("Введите элементы массива для перемножения:")).split(" ")
choice_int=[int(item) for item in choice]

if len(choice_int) < n+1:
    mult = 1
    for i in range (len(choice_int)):
        mult *= (list[choice_int[i]])
    print(mult)
else:
    print('нет столько элементов')