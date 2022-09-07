import random
n = int(input("Введите число N: "))
list = []
for i in range(0,n):
    list.append(int(random.randint(-10, 10)))
print(list)
temp=0
for i in range(0,n-1):
    temp=list[i]
    v=random.randint(0,n-1)
    list[i]=list[v]
    list[v]=temp
print(list)

