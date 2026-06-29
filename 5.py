#1 Функция, выполняющая суммирование числового ряда.
#2 Поиск степени A^P, B^P, C^P с помощью функции Power1 (A, B)
#1
def sum_series(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

n = input("Введи положительное число n: ")
while True:
    try:
        n = int(n)
        break
    except ValueError:
        print("Ты ввёл неверно.")
        n = input("Число n: ")

print("Сумма ряда от 1 до n =", sum_series(n))
#2
import math

def Power1(A, B):
    if A <= 0:
        return 0
    return math.exp(B * math.log(A))

A = float(input("Введи A: "))
B = float(input("Введи B: "))
C = float(input("Введи C: "))
P = float(input("Введи P: "))

print("A^P =", Power1(A, P))
print("B^P =", Power1(B, P))
print("C^P =", Power1(C, P))
