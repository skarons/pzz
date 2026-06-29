# Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения
# X - X^2/2 + X^3/3 - ... + (-1)^(N-1) * X^N/N.
# Полученное число является приближенным значением функции ln в точке 1 + X.

x = input("Введите вещественное число X (|X| < 1): ")
while True:
    try:
        x = float(x)
        if abs(x) >= 1:
            x = input("Число должно удовлетворять условию |X| < 1! Введите снова: ")
            continue
        break
    except ValueError:
        print("Неправильно ввели!")
        x = input("Введите вещественное число X: ")

n = input("Введите целое число N (>0): ")
while True:
    try:
        n = int(n)
        if n <= 0:
            n = input("Число N должно быть положительным! Введите снова: ")
            continue
        break
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число N: ")

s = 0
znak = 1
i = 1
while i <= n:
    s += znak * (x ** i) / i
    znak *= -1
    i += 1

print("Приближенное значение ln(1 + X) =", s)
# Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE,
# если не является — вывести FALSE.

n = input("Введите целое число N (>0): ")
while True:
    try:
        n = int(n)
        if n <= 0:
            n = input("Число N должно быть положительным! Введите снова: ")
            continue
        break
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число N: ")

temp = n
is_power = False
if temp == 1:
    is_power = True
else:
    while temp % 3 == 0:
        temp //= 3
    if temp == 1:
        is_power = True

if is_power:
    print("TRUE")
else:
    print("FALSE")
