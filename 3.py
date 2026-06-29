# Дано трехзначное число. Проверить истинность высказывания:
# «Все цифры данного числа различны».

n = input("Введите трехзначное число: ")
while True:
    try:
        n = int(n)
        if n < 100 or n > 999:
            n = input("Число должно быть трехзначным! Введите снова: ")
            continue
        break
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите трехзначное число: ")

sotni = n // 100
desyatki = (n // 10) % 10
edinitsy = n % 10

result = (sotni != desyatki) and (sotni != edinitsy) and (desyatki != edinitsy)

print("Все цифры числа различны:", result)
# Даны два числа. Вывести порядковый номер меньшего из них.

a = input("Введите первое число: ")
while True:
    try:
        a = float(a)
        break
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")

b = input("Введите второе число: ")
while True:
    try:
        b = float(b)
        break
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")

if a < b:
    print("Меньшее число - первое (номер 1)")
elif b < a:
    print("Меньшее число - второе (номер 2)")
else:
    print("Числа равны")
