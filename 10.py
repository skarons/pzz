# Практическое занятие № 10. Вариант 21. Задание 1.
# Средствами языка Python сформировать два текстовых файла (.txt), содержащих
# по одной последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно
# выполнив требуемую обработку элементов:
# Содержимое первого файла:
# Отрицательные элементы:
# Количество отрицательных элементов:
# Среднее арифметическое:
# Содержимое второго файла:
# Положительные элементы:
# Количество положительных элементов:
# Сумма положительных элементов:

# Формируем первый файл data_1.txt со списком чисел
l1 = ['-12 5 -8 23 0 -45 17 9 -3 30']
f1 = open('data_1.txt', 'w')
f1.writelines(l1)
f1.close()

# Формируем второй файл data_2.txt со списком чисел
l2 = ['14 -7 22 -19 6 33 -2 8 -25 11']
f2 = open('data_2.txt', 'w')
f2.writelines(l2)
f2.close()

# Считываем и преобразуем числа из первого файла в список целых чисел
f1 = open('data_1.txt')
k1 = f1.read()
k1 = k1.split()
for i in range(len(k1)):
    k1[i] = int(k1[i])
f1.close()

# Считываем и преобразуем числа из второго файла в список целых чисел
f2 = open('data_2.txt')
k2 = f2.read()
k2 = k2.split()
for i in range(len(k2)):
    k2[i] = int(k2[i])
f2.close()

# Обработка первого файла: отрицательные элементы, их количество и среднее
neg_elements = []
neg_count = 0
neg_sum = 0
for i in range(len(k1)):
    if k1[i] < 0:
        neg_elements.append(k1[i])
        neg_count += 1
        neg_sum += k1[i]

if neg_count > 0:
    neg_average = neg_sum / neg_count
else:
    neg_average = 0

# Обработка второго файла: положительные элементы, их количество и сумма
pos_elements = []
pos_count = 0
pos_sum = 0
for i in range(len(k2)):
    if k2[i] > 0:
        pos_elements.append(k2[i])
        pos_count += 1
        pos_sum += k2[i]

# Записываем результат обработки в итоговый файл result_1.txt
f3 = open('result_1.txt', 'w')
f3.write('Содержимое первого файла: ')
f3.write(str(k1))
f3.write('\n')
f3.write('Отрицательные элементы: ')
f3.write(str(neg_elements))
f3.write('\n')
print('Количество отрицательных элементов: ', neg_count, file=f3)
print('Среднее арифметическое: ', neg_average, file=f3)

f3.write('Содержимое второго файла: ')
f3.write(str(k2))
f3.write('\n')
f3.write('Положительные элементы: ')
f3.write(str(pos_elements))
f3.write('\n')
print('Количество положительных элементов: ', pos_count, file=f3)
print('Сумма положительных элементов: ', pos_sum, file=f3)
f3.close()

# Выводим итоговый файл на экран для проверки результата
f3 = open('result_1.txt')
print(f3.read())
f3.close()
# Практическое занятие № 10. Вариант 21. Задание 2.
# Из предложенного текстового файла (text18-21.txt) вывести на экран его
# содержимое, количество знаков препинания. Сформировать новый файл, в
# который поместить текст в стихотворной форме, выведя строки в обратном
# порядке.

# Знаки препинания, которые нужно посчитать в тексте
punctuation_marks = '.,!?;:-—()«»"\''

lines_count = 0
punctuation_count = 0

# Читаем файл построчно, выводим на экран, считаем строки и знаки препинания
# Файл сохранен в кодировке UTF-16, поэтому открываем его с указанием encoding
for line in open('text18-21.txt', encoding='UTF-16'):
    print(line, end='')
    lines_count += 1
    for symbol in line:
        if symbol in punctuation_marks:
            punctuation_count += 1

print(end='\n')
print('Количество строк: ', lines_count)
print('Количество знаков препинания: ', punctuation_count)

# Считываем все строки текста в список для дальнейшей обработки
f1 = open('text18-21.txt', encoding='UTF-16')
lines = f1.readlines()
f1.close()

# Выводим строки текста в обратном порядке
reversed_lines = lines[::-1]

# Записываем результат в новый файл в кодировке UTF-8
f2 = open('text18-21-result.txt', 'w', encoding='UTF-8')
f2.writelines(reversed_lines)
f2.close()

# Выводим итоговый файл на экран для проверки результата
print('\nСодержимое нового файла (строки в обратном порядке):')
f2 = open('text18-21-result.txt', encoding='UTF-8')
print(f2.read())
f2.close()
