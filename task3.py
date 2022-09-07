# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите число n: "))
list = []
for i in range(1, n+1):
    list.append(round(float((1 + 1/i)**i), 2))
print(list)
summ = 0
for i in range(len(list)):
    summ += list[i]
print(f"Сумма чисел равна {summ} ")
