# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random
n = int(input("Введите число N: "))
list = []
for i in range(0,n):
    list.append(int(random.randint(n*-1, n)))
print(list)

choice = []
with open("C:\work_project\python\HW_SEM2_PY_v2\data.txt") as f:
    for i in f:
        choice.append([int(x) for x in i.split(" ")])
print(choice)
print(type(choice))

choice_int=[int(item) for item in choice]

if len(choice_int) < n+1:
    mult = 1
    for i in range (len(choice_int)):
        mult *= (list[choice_int[i]])
    print(mult)
else:
    print('нет столько элементов')