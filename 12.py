# Задание 1.
# В матрице найти минимальный элемент в предпоследней строке.

try:
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    matrix = [
        [int(input(f"Элемент [{i}][{j}]: ")) for j in range(cols)]
        for i in range(rows)
    ]

    print("\nИсходная матрица:")
    for row in matrix:
        print(row)

    if rows < 2:
        print("\nОшибка: в матрице должно быть не менее двух строк.")
    else:
        min_element = min(matrix[-2])

        print("\nПредпоследняя строка:")
        print(matrix[-2])

        print(f"\nМинимальный элемент предпоследней строки: {min_element}")

except ValueError:
    print("Ошибка: необходимо вводить целые числа.")
  # Задание 2.
# В квадратной матрице элементы на главной диагонали увеличить в 2 раза.

try:
    n = int(input("Введите размер квадратной матрицы: "))

    matrix = [
        [int(input(f"Элемент [{i}][{j}]: ")) for j in range(n)]
        for i in range(n)
    ]

    print("\nИсходная матрица:")
    for row in matrix:
        print(row)

    result_matrix = [
        [
            matrix[i][j] * 2 if i == j else matrix[i][j]
            for j in range(n)
        ]
        for i in range(n)
    ]

    print("\nМатрица после увеличения элементов главной диагонали в 2 раза:")
    for row in result_matrix:
        print(row)

except ValueError:
    print("Ошибка: необходимо вводить целые числа.")
