# Задание 1.
# Даны две последовательности.
# Найти элементы, различные для двух последовательностей,
# и их среднее арифметическое.

try:
    seq1 = list(map(int, input("Введите элементы первой последовательности через пробел: ").split()))
    seq2 = list(map(int, input("Введите элементы второй последовательности через пробел: ").split()))

    print("Первая последовательность:", seq1)
    print("Вторая последовательность:", seq2)

    # Списковое включение
    unique_elements = [x for x in seq1 + seq2
                       if (x in seq1 and x not in seq2)
                       or (x in seq2 and x not in seq1)]

    print("Элементы, различные для двух последовательностей:", unique_elements)

    if unique_elements:
        average = sum(unique_elements) / len(unique_elements)
        print("Среднее арифметическое:", average)
    else:
        print("Различных элементов нет.")

except ValueError:
    print("Ошибка: необходимо вводить только целые числа.")
    # Задание 2.
# Из заданной строки отобразить только цифры.
# Использовать библиотеку string.
# Строка:
# TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC,
# 755 feet (230 metres) long and 481 feet (147 metres) high.

import string

text = ("TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, "
        "755 feet (230 metres) long and 481 feet (147 metres) high.")

print("Исходная строка:")
print(text)

# Генераторное выражение
digits = ''.join(ch for ch in text if ch in string.digits)

print("Цифры из строки:")
print(digits)
