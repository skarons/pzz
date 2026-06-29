# 1. Дан список размера N и целые числа K и L (1 < K < L < N).
#    Найти сумму всех элементов списка, кроме элементов с номерами от K до L включительно.
#
# 2. Дан целочисленный список размера N. Если он является перестановкой 1..N,
#    вывести 0; иначе вывести номер первого недопустимого элемента.
#
# 3. Даны N точек A (x и y в отдельных списках) и точка B.
#    Найти точку A, ближайшую к B.

# 1 — УДАЛЕНИЕ СРЕЗА K–L И СУММА ОСТАВШИХСЯ ЭЛЕМЕНТОВ

print("\n=== ЗАДАНИЕ 1 ===")

import random

N = int(input("Введи размер списка N: "))
K = int(input("Введи K (1 < K < L < N): "))
L = int(input("Введи L: "))

a = []
i = 0
while i < N:
    a.append(random.randint(1, 50))
    i += 1

print("Исходный список:", a)

new_list = a[:K] + a[L+1:]

print("Список без элементов K-L:", new_list)
print("Сумма оставшихся элементов:", sum(new_list))

# 2 — ПРОВЕРКА: ЯВЛЯЕТСЯ ЛИ СПИСОК ПЕРЕСТАНОВКОЙ

print("\n=== ЗАДАНИЕ 2 ===")

N2 = int(input("Размер списка N: "))

b = []
i = 0
while i < N2:
    b.append(int(input(f"Введи элемент {i+1}: ")))
    i += 1

print("Список:", b)

valid = True

for i in range(N2):
    if b[i] < 1 or b[i] > N2:
        print("Первый недопустимый элемент:", i + 1)
        valid = False
        break

if valid:
    if len(set(b)) == N2:
        print(0)
    else:
        print("Список не является перестановкой — есть повторения")

# 3 — ПОИСК БЛИЖАЙШЕЙ ТОЧКИ К B

print("\n=== ЗАДАНИЕ 3 ===")

import math

N3 = int(input("Введи количество точек N: "))

Ax = []
Ay = []

i = 0
while i < N3:
    Ax.append(float(input(f"X[{i}]: ")))
    Ay.append(float(input(f"Y[{i}]: ")))
    i += 1

Bx = float(input("Координата Bx: "))
By = float(input("Координата By: "))

min_dist = 10**9
min_index = -1

for i in range(N3):
    R = math.sqrt((Ax[i] - Bx)**2 + (Ay[i] - By)**2)
    if R < min_dist:
        min_dist = R
        min_index = i

print("\nБлижайшая точка:")
print(f"A[{min_index}] = ({Ax[min_index]}, {Ay[min_index]})")
print("Расстояние до неё:", min_dist)
